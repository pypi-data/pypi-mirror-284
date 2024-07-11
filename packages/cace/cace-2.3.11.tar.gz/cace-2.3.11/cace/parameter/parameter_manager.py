# Copyright 2024 Efabless Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re
import sys
import glob
import time
import yaml
import shutil
import signal
import datetime
import threading

from ..common.misc import mkdirp
from ..common.cace_read import cace_read, cace_read_yaml
from ..common.cace_write import (
    cace_write,
    cace_summary,
    markdown_summary,
    cace_generate_html,
)
from ..common.cace_regenerate import (
    regenerate_netlists,
    regenerate_testbenches,
)
from .physical_parameter import PhysicalParameter
from .electrical_parameter import ElectricalParameter

from ..logging import (
    verbose,
    info,
    rule,
    success,
    warn,
    err,
)
from ..logging import subprocess as subproc
from ..logging import debug as dbg


class ParameterManager:
    """
    The ParameterManager manages the parameter queue
    of physical and electrical parameters.
    It also holds the datasheet and provides functions to
    manipulate it.
    """

    def __init__(self, datasheet={}, max_runs=None, jobs=None):
        """Initialize the object with a datasheet"""
        self.datasheet = datasheet
        self.max_runs = max_runs

        self.worker_thread = None

        self.queued_threads = []
        self.queued_lock = threading.Lock()

        self.running_threads = []
        self.running_lock = threading.Lock()

        self.default_runtime_options = {
            'netlist_source': 'schematic',
            'force': False,
            'keep': False,
            'nosim': False,
            'sequential': False,
            'noplot': False,  # TODO test
            'parallel_parameters': 4,
            'debug': False,
            'filename': 'Unknown',
        }

        self.set_default_runtime_options()

        self.default_paths = {
            'templates': 'cace/templates',
            'scripts': 'cace/scripts',
        }

        self.set_default_paths()

        # Set the number of jobs to the number of cores
        # if jobs=None
        if not jobs:
            jobs = os.cpu_count()

        # Fallback jobs
        if not jobs:
            jobs = 4

        self.jobs_sem = threading.Semaphore(value=jobs)

        dbg(f'Parameter manager: total number of jobs is {jobs}')

        # Create a new run dir for logs
        self.prepare_run_dir()

    ### datasheet functions ###

    def load_datasheet(self, datasheet_path, debug):
        """
        Tries to load a datasheet from the given path.
        YAML is preferred over text format.
        Returns 0 on success and 1 on failure.
        """

        if not os.path.isfile(datasheet_path):
            err(f'File {datasheet_path} not found.')
            return 1

        [dspath, dsname] = os.path.split(datasheet_path)

        # Read the datasheet, legacy CACE ASCII format version 4.0
        if os.path.splitext(datasheet_path)[1] == '.txt':
            self.datasheet = cace_read(datasheet_path, debug)
        # Read the datasheet, new CACE YAML format version 5.0
        else:
            self.datasheet = cace_read_yaml(datasheet_path, debug)

        # CACE should be run from the location of the datasheet's root
        # directory.  Typically, the datasheet is in the "cace" subdirectory
        # and "root" is "..".

        rootpath = None
        paths = self.datasheet['paths']
        if 'root' in paths:
            rootpath = paths['root']

        if rootpath:
            dspath = os.path.join(dspath, rootpath)
            paths['root'] = '.'

        os.chdir(dspath)
        info(
            f"Working directory set to '{dspath}' ('{os.path.abspath(dspath)}')"
        )
        os.environ['CACE_ROOT'] = os.path.abspath(dspath)

        if debug:
            import pprint

            pp = pprint.PrettyPrinter()
            pp.pprint(self.datasheet)

        # Make sure all runtime options exist
        self.set_default_runtime_options()

        # Make sure all paths exist
        self.set_default_paths()

        return 0

    def find_datasheet(self, search_dir, debug):
        """
        Check the search_dir directory and determine if there
        is a .yaml or .txt file with the name of the directory, which
        is assumed to have the same name as the project circuit.  Also
        check subdirectories one level down.
        Returns 0 on success and 1 on failure.
        """

        dirname = os.path.split(search_dir)[1]
        dirlist = os.listdir(search_dir)

        # Look through all directories for a '.yaml' file
        for item in dirlist:
            if os.path.isfile(item):
                fileext = os.path.splitext(item)[1]
                basename = os.path.splitext(item)[0]
                if fileext == '.yaml':
                    if basename == dirname:
                        info(f"Loading datasheet from '{item}'")
                        self.load_datasheet(item, debug)
                        return 0

            elif os.path.isdir(item):
                subdirlist = os.listdir(item)
                for subitem in subdirlist:
                    subitemref = os.path.join(item, subitem)
                    if os.path.isfile(subitemref):
                        fileext = os.path.splitext(subitem)[1]
                        basename = os.path.splitext(subitem)[0]
                        if fileext == '.yaml':
                            if basename == dirname:
                                info(f"Loading datasheet from '{subitemref}'")
                                self.load_datasheet(subitemref, debug)
                                return 0

        # Look through all directories for a '.txt' file
        for item in dirlist:
            if os.path.isfile(item):
                fileext = os.path.splitext(item)[1]
                basename = os.path.splitext(item)[0]
                if fileext == '.txt':
                    if basename == dirname:
                        info(f"Loading datasheet from '{item}'")
                        self.load_datasheet(item, debug)
                        return 0

            elif os.path.isdir(item):
                subdirlist = os.listdir(item)
                for subitem in subdirlist:
                    subitemref = os.path.join(item, subitem)
                    if os.path.isfile(subitemref):
                        fileext = os.path.splitext(subitem)[1]
                        basename = os.path.splitext(subitem)[0]
                        if fileext == '.txt':
                            if basename == dirname:
                                info(f"Loading datasheet from '{subitemref}'")
                                self.load_datasheet(subitemref, debug)
                                return 0

        info('No datasheet found in local project (YAML or text file).')
        return 1

    def save_datasheet(self, path):
        if self.datasheet['runtime_options']['debug']:
            info(f'Writing final output file {path}')

        suffix = os.path.splitext(path)[1]

        if suffix == '.txt':
            # Write the result in legacy CACE ASCII format version 4.0
            cace_write(self.datasheet, path, doruntime=False)
        elif suffix == '.yaml':
            # Write the result in CACE YAML format version 5.0
            new_datasheet = self.datasheet.copy()

            # Rewrite internal datasheet structure
            # for format version 5.0 compatibility

            # TODO Remove this step and change the remaining code
            # in CACE to work with dictionaries

            # Convert dependencies
            if 'dependencies' in self.datasheet and self.datasheet[
                'dependencies'
            ] != [{}]:
                new_datasheet['dependencies'] = {}
                for dependency in self.datasheet['dependencies']:
                    name = dependency.pop('name')
                    new_datasheet['dependencies'][name] = dependency
            else:
                new_datasheet.pop('dependencies')

            # Convert pins
            new_datasheet['pins'] = {}
            for pin in self.datasheet['pins']:
                name = pin.pop('name')

                if 'Vmax' in pin:
                    if isinstance(pin['Vmax'], list):
                        pin['Vmax'] = ' '.join(pin['Vmax'])
                    else:
                        # Convert to float
                        try:
                            pin['Vmax'] = int(pin['Vmax'])
                        except:
                            try:
                                pin['Vmax'] = float(pin['Vmax'])
                            except:
                                pass

                if 'Vmin' in pin:
                    if isinstance(pin['Vmin'], list):
                        pin['Vmin'] = ' '.join(pin['Vmin'])
                    else:
                        # Convert to float
                        try:
                            pin['Vmin'] = int(pin['Vmin'])
                        except:
                            try:
                                pin['Vmin'] = float(pin['Vmin'])
                            except:
                                pass

                new_datasheet['pins'][name] = pin

            # Convert conditions in electrical_parameters
            for parameter in self.datasheet['electrical_parameters']:
                new_conditions = {}
                for condition in parameter['conditions']:
                    name = condition.pop('name')

                    # Convert to float
                    for limit in ['minimum', 'typical', 'maximum']:
                        if limit in condition:
                            try:
                                condition[limit] = int(condition[limit])
                            except:
                                try:
                                    condition[limit] = float(condition[limit])
                                except:
                                    pass

                    new_conditions[name] = condition
                parameter['conditions'] = new_conditions

            # Convert simulate in electrical_parameters
            for parameter in self.datasheet['electrical_parameters']:
                new_simulate = {}

                tool = parameter['simulate'].pop('tool')

                if 'format' in parameter['simulate']:
                    format_list = parameter['simulate'].pop('format')

                    parameter['simulate']['format'] = format_list[0]
                    parameter['simulate']['suffix'] = format_list[1]
                    parameter['simulate']['variables'] = format_list[2:]

                parameter['simulate'] = {tool: parameter['simulate']}

            # Convert variables in electrical_parameters
            for parameter in self.datasheet['electrical_parameters']:
                if 'variables' in parameter:
                    new_variables = {}
                    for variable in parameter['variables']:
                        name = variable.pop('name')
                        new_variables[name] = variable
                    parameter['variables'] = new_variables

            # Convert spec entries in electrical_parameters
            for parameter in self.datasheet['electrical_parameters']:
                if 'spec' in parameter:
                    for limit in ['minimum', 'typical', 'maximum']:
                        if limit in parameter['spec']:
                            new_limit = {}
                            if not isinstance(parameter['spec'][limit], list):
                                try:
                                    new_limit['value'] = int(
                                        parameter['spec'][limit]
                                    )
                                except:
                                    try:
                                        new_limit['value'] = float(
                                            parameter['spec'][limit]
                                        )
                                    except:
                                        new_limit['value'] = parameter['spec'][
                                            limit
                                        ]
                            elif len(parameter['spec'][limit]) == 2:
                                try:
                                    new_limit['value'] = int(
                                        parameter['spec'][limit][0]
                                    )
                                except:
                                    try:
                                        new_limit['value'] = float(
                                            parameter['spec'][limit][0]
                                        )
                                    except:
                                        new_limit['value'] = parameter['spec'][
                                            limit
                                        ][0]
                                new_limit['fail'] = True
                            elif len(parameter['spec'][limit]) == 3:
                                try:
                                    new_limit['value'] = int(
                                        parameter['spec'][limit][0]
                                    )
                                except:
                                    try:
                                        new_limit['value'] = float(
                                            parameter['spec'][limit][0]
                                        )
                                    except:
                                        new_limit['value'] = parameter['spec'][
                                            limit
                                        ][0]
                                new_limit['fail'] = True
                                new_limit['calculation'] = parameter['spec'][
                                    limit
                                ][2]

                            parameter['spec'][limit] = new_limit

            # Convert evaluate in physical_parameters
            for parameter in self.datasheet['physical_parameters']:
                tool = parameter['evaluate'].pop('tool')
                new_evaluate = tool

                if isinstance(tool, list):
                    if tool[0] == 'cace_lvs':
                        parameter['evaluate']['script'] = tool[1]
                        tool = 'cace_lvs'
                    else:
                        err(f'Unknown tool list {tool}')

                if parameter['evaluate']:
                    new_evaluate = {tool: parameter['evaluate']}
                else:
                    new_evaluate = tool

                parameter['evaluate'] = new_evaluate

            # Convert spec entries in physical_parameters
            for parameter in self.datasheet['physical_parameters']:
                if 'spec' in parameter:
                    for limit in ['minimum', 'typical', 'maximum']:
                        if limit in parameter['spec']:
                            new_limit = {}
                            if not isinstance(parameter['spec'][limit], list):
                                try:
                                    new_limit['value'] = int(
                                        parameter['spec'][limit]
                                    )
                                except:
                                    try:
                                        new_limit['value'] = float(
                                            parameter['spec'][limit]
                                        )
                                    except:
                                        new_limit['value'] = parameter['spec'][
                                            limit
                                        ]
                            elif len(parameter['spec'][limit]) == 2:
                                try:
                                    new_limit['value'] = int(
                                        parameter['spec'][limit][0]
                                    )
                                except:
                                    try:
                                        new_limit['value'] = float(
                                            parameter['spec'][limit][0]
                                        )
                                    except:
                                        new_limit['value'] = parameter['spec'][
                                            limit
                                        ][0]
                                new_limit['fail'] = True
                            elif len(parameter['spec'][limit]) == 3:
                                try:
                                    new_limit['value'] = int(
                                        parameter['spec'][limit][0]
                                    )
                                except:
                                    try:
                                        new_limit['value'] = float(
                                            parameter['spec'][limit][0]
                                        )
                                    except:
                                        new_limit['value'] = parameter['spec'][
                                            limit
                                        ][0]
                                new_limit['fail'] = True
                                new_limit['calculation'] = parameter['spec'][
                                    limit
                                ][2]

                            parameter['spec'][limit] = new_limit

            # Convert default_conditions
            new_datasheet['default_conditions'] = {}
            for default_condition in self.datasheet['default_conditions']:
                name = default_condition.pop('name')

                # Convert to float
                for limit in ['minimum', 'typical', 'maximum']:
                    if limit in default_condition:
                        try:
                            default_condition[limit] = int(
                                default_condition[limit]
                            )
                        except:
                            try:
                                default_condition[limit] = float(
                                    default_condition[limit]
                                )
                            except:
                                pass

                new_datasheet['default_conditions'][name] = default_condition

            # Convert electrical_parameters
            new_datasheet['electrical_parameters'] = {}
            for electrical_parameter in self.datasheet[
                'electrical_parameters'
            ]:
                name = electrical_parameter.pop('name')
                new_datasheet['electrical_parameters'][
                    name
                ] = electrical_parameter

            # Convert physical_parameters
            new_datasheet['physical_parameters'] = {}
            for physical_parameter in self.datasheet['physical_parameters']:
                name = physical_parameter.pop('name')
                new_datasheet['physical_parameters'][name] = physical_parameter

            # Rewrite paths['root'] as the cwd relative to filename.
            oldroot = None
            if 'paths' in new_datasheet:
                paths = new_datasheet['paths']
                if 'root' in paths:
                    oldroot = paths['root']
                    filepath = os.path.split(path)[0]
                    newroot = os.path.relpath(os.curdir, filepath)
                    paths['root'] = newroot

            # Remove runtime options
            new_datasheet.pop('runtime_options')

            # Set version to 5.0
            new_datasheet['cace_format'] = 5.0

            with open(os.path.join(path), 'w') as outfile:
                yaml.dump(
                    new_datasheet,
                    outfile,
                    default_flow_style=False,
                    sort_keys=False,
                    allow_unicode=True,
                )
        else:
            warn(f'Unsupported file extension: {suffix}')

    def set_datasheet(self, datasheet):
        """Set a new datasheet"""
        self.datasheet = datasheet

    def get_datasheet(self):
        """Return the datasheet"""
        return self.datasheet

    def summarize_datasheet(self):
        return markdown_summary(self.datasheet)

    def generate_html(self):
        debug = self.get_runtime_options('debug')
        cace_generate_html(self.datasheet, None, debug)

    def duplicate_parameter(self, pname):
        param = self.find_parameter(pname)

        if not param:
            warn(f'Could not duplicate parameter {pname}')
            return

        newparam = param.copy()

        # Make the copied parameter editable
        newparam['editable'] = True

        # Adjsut the name
        newparam['name'] += '_copy'

        # Append this to the electrical parameter list after the item being copied
        if 'display' in param:
            newparam['display'] = param['display'] + ' (copy)'

        eparams = self.datasheet['electrical_parameters']
        eidx = eparams.index(param)
        eparams.insert(eidx + 1, newparam)

    def delete_parameter(self, pname):
        param = self.find_parameter(pname)

        if not param:
            warn(f'Could not delete parameter {pname}')
            return

        eparams = self.datasheet['electrical_parameters']
        eidx = eparams.index(param)
        eparams.pop(eidx)

    def set_default_runtime_options(self):
        """Sane default values"""

        # Make sure runtime options exist
        if not 'runtime_options' in self.datasheet:
            self.datasheet['runtime_options'] = {}

        # Init with default value if key does not exist
        for key, value in self.default_runtime_options.items():
            if not key in self.datasheet['runtime_options']:
                self.datasheet['runtime_options'][key] = value

    def set_default_paths(self):
        """Sane default values"""

        # Make sure runtime options exist
        if not 'paths' in self.datasheet:
            self.datasheet['paths'] = {}

        # Init with default value if key does not exist
        for key, value in self.default_paths.items():
            if not key in self.datasheet['paths']:
                self.datasheet['paths'][key] = value

    def set_runtime_options(self, key, value):
        self.datasheet['runtime_options'][key] = value

        # Make sure the runtime options are valid
        self.validate_runtime_options()

    def get_runtime_options(self, key):
        if not key in self.datasheet['runtime_options']:
            dbg(f'Runtime option "{key}" not in runtime_options')
            if key in self.default_options:
                info(f'Setting runtime option "{key}" to default value')
                self.datasheet['runtime_options'][key] = self.default_options[
                    key
                ]

        return self.datasheet['runtime_options'][key]

    def get_path(self, key):
        if not key in self.datasheet['paths']:
            dbg(f'Path "{key}" not in paths')
            dbg(f'Setting path "{key}" to "{key}"')
            self.datasheet['paths'][key] = key

        return self.datasheet['paths'][key]

    def validate_runtime_options(self):
        """Make sure the runtime options contain valid values"""

        valid_sources = ['schematic', 'layout', 'pex', 'rcx', 'best']

        if (
            not self.datasheet['runtime_options']['netlist_source']
            in valid_sources
        ):
            err(
                f'Invalid netlist source: {self.datasheet["runtime_options"]["netlist_source"]}'
            )

        if not self.datasheet['runtime_options']['parallel_parameters'] > 0:
            err(f'parallel_parameters must be at least 1')

        # TODO check that other keys exist

    ### simulation functions ####

    def get_all_pnames(self):
        """Return all parameter names"""

        eparams = []
        pparams = []

        if 'electrical_parameters' in self.datasheet:
            eparams = [
                item['name']
                for item in self.datasheet['electrical_parameters']
            ]

        if 'physical_parameters' in self.datasheet:
            pparams = [
                item['name'] for item in self.datasheet['physical_parameters']
            ]

        return eparams + pparams

    def find_parameter(self, pname):
        """
        Searches for the parameter with the name pname
        """

        # TODO make 'electrical_parameters' and 'physical_parameters'
        # a dictionary for much easier access

        param = None

        if 'electrical_parameters' in self.datasheet:
            for item in self.datasheet['electrical_parameters']:
                if item['name'] == pname:
                    if param:
                        err(f'{pname} at least twice in datasheet')
                    param = item

        if 'physical_parameters' in self.datasheet:
            for item in self.datasheet['physical_parameters']:
                if item['name'] == pname:
                    if param:
                        err(f'{pname} at least twice in datasheet')
                    param = item

        if not param:
            warn(f'Unknown parameter: {pname}')
            if 'electrical_parameters' in self.datasheet:
                warn('Known electrical parameters are:')
                for eparam in self.datasheet['electrical_parameters']:
                    warn(eparam['name'])
            if 'physical_parameters' in self.datasheet:
                warn('Known physical parameters are:')
                for pparam in self.datasheet['physical_parameters']:
                    warn(pparam['name'])

        return param

    def param_set_status(self, pname, status):
        param = self.find_parameter(pname)
        if param:
            param['status'] = status

    def queue_parameter(
        self, pname, start_cb=None, end_cb=None, cancel_cb=None, step_cb=None
    ):
        """Queue a parameter for later execution"""

        paths = self.datasheet['paths']
        runtime_options = self.datasheet['runtime_options']
        pdk = self.datasheet['PDK']

        if 'electrical_parameters' in self.datasheet:
            for param in self.datasheet['electrical_parameters']:
                if param['name'] == pname:
                    # Quick check for skipped or blocked parameter.
                    if 'status' in param:
                        status = param['status']
                        if status == 'skip':
                            warn(
                                f'Skipping parameter {param["name"]} (status=skip).'
                            )
                            return
                        if status == 'blocked':
                            warn(
                                f'Skipping parameter {param["name"]} (status=blocked).'
                            )
                            return

                    new_sim_param = ElectricalParameter(
                        param,
                        self.datasheet,
                        pdk,
                        paths,
                        runtime_options,
                        self.run_dir,
                        self.jobs_sem,
                        start_cb,
                        end_cb,
                        cancel_cb,
                        step_cb,
                    )

                    dbg(
                        f'Inserting electrical parameter {param["name"]} into queue'
                    )

                    with self.queued_lock:
                        self.queued_threads.insert(0, new_sim_param)

                    # TODO return number of simulations for this parameter
                    #      needed for progress bars etc.
                    return 1

        if 'physical_parameters' in self.datasheet:
            for param in self.datasheet['physical_parameters']:
                if param['name'] == pname:
                    # Quick check for skipped or blocked parameter.
                    if 'status' in param:
                        status = param['status']
                        if status == 'skip':
                            warn(
                                f'Skipping parameter {param["name"]} (status=skip).'
                            )
                            return
                        if status == 'blocked':
                            warn(
                                f'Skipping parameter {param["name"]} (status=blocked).'
                            )
                            return

                    new_sim_param = PhysicalParameter(
                        param,
                        self.datasheet,
                        pdk,
                        paths,
                        runtime_options,
                        self.run_dir,
                        self.jobs_sem,
                        start_cb,
                        end_cb,
                        cancel_cb,
                        step_cb,
                    )

                    dbg(
                        f'Inserting physical parameter {param["name"]} into queue'
                    )

                    with self.queued_lock:
                        self.queued_threads.insert(0, new_sim_param)

                    # TODO return number of simulations for this parameter
                    #      needed for progress bars etc.
                    return 1

        warn(f'Unknown parameter {pname}')
        if 'electrical_parameters' in self.datasheet:
            warn('Known electrical parameters are:')
            for eparam in self.datasheet['electrical_parameters']:
                warn(eparam['name'])
        if 'physical_parameters' in self.datasheet:
            warn('Known physical parameters are:')
            for pparam in self.datasheet['physical_parameters']:
                warn(pparam['name'])

        return None

    def prune_running_threads(self):
        """Remove threads that are either marked as done or have been canceled"""

        needs_unlock = False
        if not self.running_lock.locked():
            self.running_lock.lock()
            needs_unlock = True

        # Remove completed threads
        self.running_threads = [
            t
            for t in self.running_threads
            if t.is_alive() or (not t.done and not t.canceled)
        ]

        if needs_unlock:
            self.running_lock.unlock()

    def num_parameters(self):
        """Get the number of queued or running parameters"""

        return self.num_queued_parameters() + self.num_running_parameters()

    def num_queued_parameters(self):
        """Get the number of queued parameters"""

        return len(self.queued_threads)

    def num_running_parameters(self):
        """Get the number of running parameters"""

        with self.running_lock:
            self.prune_running_threads()

            # Count the parameter threads that are not yet done
            num_running = sum(
                1
                for t in self.running_threads
                if not t.done and not t.canceled
            )

        return num_running

    def prepare_run_dir(self):

        self.design_dir = '.'

        # Create a new tag
        tag = (
            datetime.datetime.now()
            .astimezone()
            .strftime('RUN_%Y-%m-%d_%H-%M-%S')
        )

        # Create new run dir
        self.run_dir = os.path.abspath(
            os.path.join(self.design_dir, 'runs', tag)
        )

        # Check if run dir already exists
        runs = sorted(glob.glob(os.path.join(self.design_dir, 'runs', '*')))

        if self.run_dir in runs:
            error('Run directory exists already. Please try again.')

        info(f"Starting a new run with the tag '{tag}'.")
        mkdirp(self.run_dir)

        # Delete the oldest runs if max_runs set TODO only works for >=2
        if self.max_runs and len(runs) >= self.max_runs:
            runs = runs[::-1]   # Reverse runs
            # Select runs to remove
            remove = runs[self.max_runs - 1 :]
            dbg(f'Removing run directories: {remove}')

            for run in remove:
                shutil.rmtree(run)

    def run_parameters_async(self):
        """Start a worker thread to start parameter threads"""

        # Start by regenerating the netlists for the circuit-under-test
        # (This may not be quick but all tests depend on the existence
        # of the netlist, so it has to be done here and cannot be
        # parallelized).

        fullnetlistpath = regenerate_netlists(self.datasheet)
        if not fullnetlistpath:
            err('Failed to regenerate project netlist, aborting.')
            self.cancel_parameters(True)
            return

        # Next, for each parameter generate testbench netlists if needed
        for thread in self.queued_threads:
            result = regenerate_testbenches(
                self.datasheet, thread.param['name']
            )
            if result == 1:
                err(
                    f'Parameter {self.param["name"]}: Failed to regenerate testbench netlists'
                )
                return 1

        # Only start a new worker thread, if
        # the previous one hasn't completed yet
        if not self.worker_thread or not self.worker_thread.is_alive():
            # Start new worker thread to start parameter threads
            self.worker_thread = threading.Thread(
                target=self.run_parameters_thread
            )
            self.worker_thread.start()

    def run_parameters_thread(self):
        """Called as a thread, starts the threads of queued parameters"""

        while self.queued_threads:

            # Check whether we can start another parameter in parallel
            if (
                self.num_running_parameters()
                < self.datasheet['runtime_options']['parallel_parameters']
            ):
                param_thread = None

                # Holding both locks, move a parameter
                # from queued to running
                with self.running_lock:
                    with self.queued_lock:
                        # Could have been cancelled meanhwile
                        if self.queued_threads:
                            param_thread = self.queued_threads.pop()
                            self.running_threads.append(param_thread)

                if param_thread and not param_thread.canceled:
                    dbg(f'Running parameter {param_thread.param["name"]}')
                    param_thread.start()

            # Else wait until another parameter has completed
            else:
                time.sleep(0.1)

    def join_parameters(self):
        """Join all running parameter threads"""

        # Wait until all parameters are running
        if self.worker_thread:
            self.worker_thread.join()
        self.worker_thread = None

        # Wait until all parameters are complete
        with self.running_lock:
            for param_thread in self.running_threads:
                param_thread.join()

            # Remove completed threads
            self.prune_running_threads()

    def run_parameters(self):
        """Run parameters sequentially, note that simulations can still be parallelized"""

        with self.queued_lock:
            while self.queued_threads:
                param_thread = self.queued_threads.pop()
                param_thread.run()

    def cancel_parameters(self, no_cb=False):
        """Cancel all parameters"""

        self.cancel_queued_parameters(no_cb)
        self.cancel_running_parameters(no_cb)

    def cancel_queued_parameters(self, no_cb=False):
        """Cancel all queued parameters"""

        with self.queued_lock:
            while self.queued_threads:
                param_thread = self.queued_threads.pop()

                # Cancel the thread and start it
                # so that it directly calls its callback
                param_thread.cancel(no_cb)
                param_thread.start()

    def cancel_running_parameters(self, no_cb=False):
        """Cancel all running parameters"""

        with self.running_lock:

            # Remove completed threads
            self.prune_running_threads()

            for param_thread in self.running_threads:
                param_thread.cancel(no_cb)

    def cancel_parameter(self, pname, no_cb=False):
        """Cancel a single parameter"""

        self.cancel_queued_parameter(pname, no_cb)
        self.cancel_running_parameter(pname, no_cb)

    def cancel_queued_parameter(self, pname, no_cb=False):
        """Cancel a single running parameter"""

        with self.queued_lock:

            # Get all threads that should be canceled
            # Maybe there are multiple threads with the same name
            cancel_threads = [
                t for t in self.queued_threads if t.param['name'] == pname
            ]

            for param_thread in cancel_threads:

                # Remove the thread from the queued list
                self.queued_threads.remove(param_thread)

                # Cancel the thread and start it
                # so that it directly calls its callback
                param_thread.cancel(no_cb)
                param_thread.start()

    def cancel_running_parameter(self, pname, no_cb=False):
        """Cancel a single running parameter"""

        with self.running_lock:

            # Remove completed threads
            self.prune_running_threads()

            for param_thread in self.running_threads:
                # TODO also check source
                if param_thread.param['name'] == pname:
                    param_thread.cancel(no_cb)
