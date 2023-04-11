"""
The glyphcast.utils module consists of miscelleneous helper methods for spawning subprocesses and
creating human-readable file size strings for logging messages
"""

import logging
import subprocess

from typing import List


def execute(cmd: List, raise_error=True) -> int:
    """ Execute the command CMD as a subprocess, returning the exit code integer
        Logs any stdout output from the subprocess as a debug message
    """
    popen = subprocess.Popen(
        cmd,
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    for stdout_line in iter(popen.stdout.readline, ""):
        # TODO: Change this print message to a logging message
        logging.debug(stdout_line)
    popen.stdout.close()
    return_code = popen.wait()
    if return_code and raise_error:
        logging.error(f"Command {cmd} failed with return code {return_code}")
        raise subprocess.CalledProcessError(return_code, cmd)
    return return_code

def human_size(bytes_):
    if bytes_ < 1000 * 1000:
        conversion_factor = 1/1000
        units = "kb"
    else:
        conversion_factor = 1/(1000*1000)
        units = "mb"
    converted = bytes_ * conversion_factor
    return f"{converted:.1f} {units}"
