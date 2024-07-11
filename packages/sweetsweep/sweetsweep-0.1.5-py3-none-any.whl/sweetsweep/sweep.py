#!/usr/bin/env python3

import os
import time
import csv
import io
import sys

from .common import *

# TODO: Make a class instead of just functions, it will make passing arguments internally easier.
#  - Make it so that there is less boilerplate code
#  - Either call a sweetsweep method to register each image name, or have the viewer scan the directories and propose all unique filenames

# This function performs a parameter sweep.
# It calls `experiment_func` with all combinations of possible parameter values listed in `param_dict`.
# - param_dict: `dict` where each (key,value) is respectively:
#                   - the parameter name
#                   - a `list` of all values (can be numbers, strings, booleans, etc.) to sweep for that parameter
# - experiment_func: a functor that takes as argument :
#                    - an experiment index (int)
#                    - a dictionary with a single value for each parameter.
#                    - if `sweep_dir` is not empty, a path to the experiment directory
# - sweep_dir: the main directory in which to store all the experiment directories
# - start_index: optional argument that sets the first experiment ID.
# - result_csv_filename: an optional CSV filename to write individual results of each experiment. Each experiment will
#                        have one row in that CSV. If this is set, then experiment_func must return the results as a
#                        dictionary, with keys being the column names, and values the value of each result for that
#                        experiment. The results are written individually to the file as soon as they are obtained,
#                        so that the file is readable during the sweep.
# - specific_dict: a dictionary containing the swept parameters that are specific to certain values of other
#                  swept parameters. This will avoid computing redundant experiments. Example: if your sweep is
#                  {"alpha":["A","B","C"],"beta":[1,2,3]}, but 'beta' only changes the result of the experiment when
#                  'alpha'="B", then set specific_dict={"beta":{"alpha":"B"}}. This way, the redundant experiments
#                  of different values of 'beta' when 'alpha" = "A" or "C" will not be computed.
# - skip_exps: a dictionary (or a list of dictionaries) of the sets of experiments to skip. Example: if your sweep is
#              {"alpha":["A","B","C"],"beta":[1,2,3],"gamma":[0.5,0.6,0.7]}, and you know that "gamma"=0.7 is good for
#              "beta"=1 or 2, but isn't relevant for 3, you can skip it by passing skip_exps={"gamma":0.7,"beta":3}.
#              Use a list of dictionaries if there are multiple independent conditions to skip.
# - only_exp_id: an integer indicating an experiment index. Only the experiment corresponding to this id will be run
#               instead of the whole sweep. This is useful when doing sweeps on a cluster, e.g. for array jobs.
#               Values must be between 0 and the total number of experiments.
def parameter_sweep(param_dict, experiment_func, sweep_dir, start_index=0, result_csv_filename="", specific_dict=None,
                    skip_exps=None, only_exp_id=None):

    # Logger that duplicates terminal output to file
    logger = Logger(os.path.join(sweep_dir,"output.txt"))

    if not param_dict:
        print("The parameter dictionary is empty. Nothing to do.")
        return

    # Set some variables
    csv_path = os.path.join(sweep_dir, result_csv_filename)

    # Fill the current_dict and count number of experiments
    current_dict = {}
    num_exp = 1
    for k in param_dict.keys():
        current_dict[k] = param_dict[k][0]
        num_exp *= len(param_dict[k])

    if start_index < 0:
        print("ERROR: start_index (%d) must be >= 0"%start_index)

    if only_exp_id is not None:
        if only_exp_id > start_index + num_exp-1 or only_exp_id < start_index:
            print("ERROR: The exp_id provided (%d) must be between %d and %d"%(only_exp_id,start_index,start_index+num_exp-1))
        else:
            print("\nRunning 1 experiment out of", num_exp, "in total.\n")
    else:
        print("\nThere are",num_exp,"experiments in total.\n")

    # if specific_dict:
    #     num_unique_exp = get_num_unique_exp(param_dict,specific_dict)
    #     print("There are %d unique experiments and %d redundant ones"%(num_unique_exp,num_exp-num_unique_exp))

    def recursive_call(exp_id, current_dict, param_index):
        current_key = list(param_dict.keys())[param_index]
        for v in param_dict[current_key]:
            current_dict[current_key] = v
            if param_index != len(param_dict.keys())-1:
                exp_id = recursive_call(exp_id, current_dict, param_index+1)
            else:
                # print("\nExperiment #%d:" % exp_id, current_dict)

                # Check if need to skip this experiment
                if (only_exp_id is not None and only_exp_id != exp_id) or \
                        (skip_exps is not None and check_skip_exp(current_dict, skip_exps)):
                    # print("Skipping")
                    exp_id = exp_id + 1
                    continue

                # Get folder name for that experiment
                exp_dir = os.path.join(sweep_dir, build_dir_name(num_exp, exp_id, current_dict))

                # Check whether this experiment is redundant
                src_exp_id, src_exp_dict = check_exp_redundancy(param_dict, specific_dict, current_dict, start_index)

                # Write the csv row prefix
                csv_row_prefix = ""
                if result_csv_filename:
                    csv_row_prefix = [exp_id, src_exp_id] + list(current_dict.values())

                # If it's redundant, make a symlink to the source experiment directory
                if src_exp_id != -1:
                    # Get the src dir name
                    src_exp_dir = build_dir_name(num_exp, src_exp_id, src_exp_dict)
                    # Make the symlink
                    try:
                        os.symlink(src_exp_dir, exp_dir, target_is_directory=True)
                    except FileExistsError:
                        pass

                    # The results are the same as for src_exp_id, so don't rewrite them,
                    # 'src_exp_id" in the csv_row_prefix leads to the source experiment
                    result_dict = {}

                # Otherwise, run the experiment
                else:
                    # Make the directory
                    os.makedirs(exp_dir, exist_ok=True)
                    # Run the experiment
                    result_dict = experiment_func(exp_id, current_dict, exp_dir)

                    if not result_dict:
                        print("WARNING: Experiment %d - can't write results to CSV, didn't receive results "
                                "from experiment_func()." % exp_id)

                if result_csv_filename:
                    # Write the header (does nothing if already written)
                    csv_write_header(csv_path, current_dict, result_dict)

                    # Write results to the CSV
                    csv_write_result(csv_path, csv_row_prefix, result_dict)

                exp_id = exp_id + 1

        return exp_id

    # Start experiments
    t0 = time.time()
    recursive_call(start_index, current_dict, 0)
    print("Total time of all experiments:",time.time()-t0)


# Logger that duplicates output to terminal and to file
# Not portable on Windows though...
class Logger(object):

    def __init__(self,logfile):
        # import warnings
        # warnings.filterwarnings("default")

        # Works but we loose colors in the terminal
        import subprocess
        self.tee = subprocess.Popen(["tee", logfile], stdin=subprocess.PIPE)
        os.dup2(self.tee.stdin.fileno(), sys.stdout.fileno())
        os.dup2(self.tee.stdin.fileno(), sys.stderr.fileno())

    def __del__(self):
        self.tee.stdin.close()
        sys.stdout.close()
        sys.stderr.close()



# Write results of one experiment in the CSV (one single line)
def csv_write_result(csv_path, csv_row_prefix, result_dict={}):
    # Save additional results by writing them to the CSV
    with open(csv_path, mode='a') as csv_file:
        csv_writer = csv.writer(csv_file,quoting=csv.QUOTE_NONNUMERIC)
        csv_row = csv_row_prefix + list(result_dict.values())  # Write returned data
        csv_writer.writerow(csv_row)


# This function writes the header of the CSV file if it's not written yet
# If the file doesn't exist, it creates it and adds the header
# If the file exists but doesn't start with the header, it prepends it.
# This can happen when experiments are not run in the natural order,
# i.e. when a redundant experiment is run before its source experiment.
#
# One issue with this way of doing things is that when all experiments
# finish at the same time, then the csv file can have mistakes, like the
# header may appear twice, and/or some lines might be missing as they are
# overwritten by another experiment. This is very rare, and if it happens,
# Put a delay e.g. proportional to exp_id, to avoid that situation.
# I tried to fix it with threading.Lock(), but it didn't work...
# If I wanted to debug it further, I could look at the different states
# the csv file goes through at that time, maybe using auditctl?
# https://unix.stackexchange.com/a/12251/120494
def csv_write_header(csv_path, current_dict, result_dict):
    # Check if header exists
    file_exists = os.path.exists(csv_path)
    if file_exists:
        if file_get_first_line(csv_path).startswith('"exp_id"'):
            return

    # Build the CSV header
    header_line = io.StringIO()
    writer = csv.writer(header_line,quoting=csv.QUOTE_NONNUMERIC)
    csv_header = ["exp_id", "src_exp_id"] + list(current_dict.keys()) + list(result_dict.keys())
    writer.writerow(csv_header)
    header_str = header_line.getvalue()

    # Write the header
    if not file_exists:
        # Create the csv file and write the header.
        with open(csv_path, mode='w') as f:
            f.write(header_str)
    else:
        # If file exists, then the first line can't be a header,
        # otherwise we would have returned early.
        file_prepend_line(csv_path, header_str)


def file_get_first_line(filename):
    with open(filename) as f:
        return f.readline()


# https://stackoverflow.com/a/5917395/4195725
def file_prepend_line(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


def get_num_exp(sweep_dict):
    num_exp = 1
    for k in sweep_dict.keys():
        num_exp *= len(sweep_dict[k])
    return num_exp


# def get_num_unique_exp(sweep_dict,specific_dict):
#
#     for param,value_list in sweep_dict.items():
#         if param in specific_dict:
#
#         else:
#             total *= len(value_list)
#
#     return 0


def build_dir_name(n_exp, exp_id, current_dict):
    exp_dir = ("exp_%0" + str(len(str(n_exp))) + "d_") % exp_id
    for k, v in current_dict.items():
        exp_dir += "_" + k + (v if isinstance(v,str) else "%g"%v)
    return exp_dir


def get_exp_id(sweep_dict, current_dict):
    if sweep_dict.keys() != current_dict.keys():
        print("ERROR: Dictionaries don't have the same keys. Aborting.")
        exit(-1)
    # Go through the dict in reverse to get number of leaves of the sub-tree
    dict_items = list(current_dict.items())
    dict_items.reverse()
    cum_prod = 1    # Number of leaves in the subtree
    index = 0
    for k,v in dict_items:
        v_index = sweep_dict[k].index(v)
        index += v_index*cum_prod
        cum_prod *= len(sweep_dict[k])
    return index


# Check whether an experiment is redundant or not, based on a specificity dictionary
# If it is, it returns the id and param dictionary of the experiment to copy from
def check_exp_redundancy(sweep_dict, specific_dict, current_dict, start_index):

    if not specific_dict:
        return -1, {}

    # Get the list of parameters to change (to the first value of their list) to find the src experiment
    param_change = []
    for k2, v2 in specific_dict.items():
        if not k2 in sweep_dict:
            print("ERROR: parameter '%s' is not in sweep_dict." % k2)
            exit(-1)
        # If the current exp doesn't match the condition, compute only for the first value of the
        # parameter (could be any of them), and for the others, make symbolic links.
        match_condition = True
        for k3, v3 in v2.items():
            if not isinstance(v3,list): v3 = [v3]  # Support lists and singletons
            if not k3 in sweep_dict:
                print("ERROR: parameter '%s' is not in sweep_dict."%k3)
                exit(-1)
            if not set(v3).issubset(sweep_dict[k3]):
                print("ERROR: some values for '%s' in specific_dict are not in sweep_dict:"%k3)
                print("sweep_dict:", sweep_dict)
                print("specific_dict['%s']:"%k3, v3)
                exit(-1)
            match_condition &= (current_dict[k3] in v3)
            # if current_dict[k3] in v3: print("match condition", k3, "in", v3)
        if current_dict[k2] != sweep_dict[k2][0] and not match_condition:
            param_change.append(k2)
            # print("Symlink", k2)

    # Find the source folder: the one that has the results we would get if we ran this experiment.
    # It's the one for which the params in param_change have the first value of their swept list.
    if param_change:
        src_dict = current_dict.copy()
        for p in param_change:
            src_dict[p] = sweep_dict[p][0]
        src_exp_id = start_index + get_exp_id(sweep_dict, src_dict)
        # print("-> symlink to exp #%d"%src_exp_id,":",src_dict)
        return src_exp_id, src_dict
    else:
        return -1, {}


def check_skip_exp(current_dict, skip_exps):
    if not isinstance(skip_exps, list):
        skip_exps = [skip_exps]
    for condition in skip_exps:
        skip = True
        if not condition: continue
        for k,v in condition.items():
            if not isinstance(v,list): v = [v]
            if not k in current_dict:
                print("ERROR: parameter '%s' is not in current_dict." % k)
            if current_dict[k] not in v:
                skip = False
                break
        if skip:
            return True
    return False


# Make list of parameter dictionaries (one for each experiment)
def make_param_dict_list(param_dict):
    return make_param_dict_list_recursive(param_dict, {}, 0)


# Recursive function to make list of parameter dictionaries
def make_param_dict_list_recursive(param_dict, current_dict, param_index):
    current_key = list(param_dict.keys())[param_index]
    param_dict_list = []
    for v in param_dict[current_key]:
        current_dict[current_key] = v
        if param_index == len(param_dict.keys())-1:
            param_dict_list.append(current_dict.copy())
        else:
            param_dict_list += make_param_dict_list_recursive(param_dict, current_dict, param_index+1)

    return param_dict_list


##################
# PARALLEL SWEEP #
##################


# Same function as above, except that it runs the sweep with a multiprocessing pool of `max_workers` workers.
# The results are written individually to the CSV file as they are produced, so that it's always readable
# during the sweep
def parameter_sweep_parallel(param_dict, experiment_func, sweep_dir, max_workers=4, start_index=0, result_csv_filename=""):

    import pathos.multiprocessing as mp
    # import multiprocessing as mp
    from pathos.helpers import mp as pathos_multiprocess
    import contextlib
    
    # Function to print to file
    def print_to_file(file,print_str):
        with open(file, mode='a+') as f:
            f.write(print_str+"\n")

    # Function to print to stdout and to file
    def multiple_print(print_str,stdout=True,f_output=True,f_output_ordered=True):
        if stdout: print(print_str)
        if f_output: print_to_file(os.path.join(sweep_dir,"output.txt"),print_str)
        if f_output_ordered: print_to_file(os.path.join(sweep_dir,"output-ordered.txt"),print_str)

    if not param_dict:
        print("The parameter dictionary is empty. Nothing to do.")
        return

    # Fill the current_dict and count number of experiments
    current_dict={}
    num_exp = 1
    for k in param_dict.keys():
        current_dict[k] = param_dict[k][0]
        num_exp *= len(param_dict[k])

    multiple_print("There are %d experiments in total.\n"%num_exp)

    # Get list of parameter dictionaries (one for each experiment)
    param_dict_list = make_param_dict_list(param_dict)

    # Experiment worker
    def worker_run_experiment(exp_id, current_dict, result_queue):
        # Create a folder for that experiment
        exp_dir = os.path.join(sweep_dir, ("exp_%0" + str(len(str(num_exp))) + "d_") % exp_id)
        for k, v in current_dict.items():
            exp_dir += "_" + k + str(v)
        os.makedirs(exp_dir, exist_ok=True)

        print("\nExperiment %d: START\n"%exp_id)    # Indicates when each experiment starts
        # Redirect stdout and stderr in buffer variable
        with contextlib.redirect_stdout(io.StringIO()) as buff_out, contextlib.redirect_stderr(sys.stdout):

            # Run the experiment
            result_dict = experiment_func(exp_id, current_dict, exp_dir)
            
            # Get stdout
            exp_stdout = buff_out.getvalue()

        # Experiments are finished when their output is printed
        multiple_print(exp_stdout,stdout=True,f_output=True,f_output_ordered=False)

        # Send to queue to write results
        if result_csv_filename:
            if result_dict:
                result_queue.put((exp_id, current_dict, result_dict))
            else:
                multiple_print("WARNING: Experiment %d - can't write results to CSV, received 'None' from experiment_func()."%exp_id)

        return result_dict, exp_stdout

    # Result writing listener
    def write_results_to_csv(result_queue):

        write_header = True
        # Be careful, i doesn't represent the exp_id, they usually don't terminate in order.
        # It's just because we know we should receive a total of `num_exp` results.
        for i in range(num_exp):
            exp_id, exp_param_dict, result_dict = result_queue.get()

            # Save additional results by writing them to the CSV
            with open(os.path.join(sweep_dir, result_csv_filename), mode='a') as csv_file:
                csv_writer = csv.writer(csv_file,quoting=csv.QUOTE_NONNUMERIC)
                # Only on first call received, write the CSV header
                if write_header:
                    csv_writer.writerow(["exp_id"] + list(exp_param_dict.keys()) + list(result_dict.keys()))
                    write_header = False
                # Write the result row
                csv_row = [exp_id] + list(exp_param_dict.values())  # Write exp_id and current param values
                csv_row += list(result_dict.values())  # Write returned data
                csv_writer.writerow(csv_row)

    # Must use Manager queue here, or will not work
    manager = pathos_multiprocess.Manager()
    queue = manager.Queue()

    # Run experiments
    t0 = time.time()
    with mp.Pool(max_workers) as pool:
        # Put listener to work first
        watcher = pool.apply_async(write_results_to_csv, (queue,))
        # Spawn workers
        res = pool.starmap(worker_run_experiment, zip(range(start_index,num_exp+start_index), param_dict_list, [queue]*num_exp))
    
    # Print outputs
    multiple_print("".join([r[1] for r in res]),stdout=False,f_output=False,f_output_ordered=True)
    multiple_print("Total time of all experiments: %g"%(time.time()-t0))

