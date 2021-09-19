"""Utilities for Python hooks.

Mainly, executing external processes.
"""

import contextlib
import os
import pathlib
import shutil
import subprocess  # nosec
import sys


def unique_directories(files):
    """Returns a list of directories (pathlib.Path objects) for the files
    passed without repetitions."""
    return list({pathlib.Path(x).parent for x in files})


@contextlib.contextmanager
def chdir(path):
    """Context manager for changing the working directory.

    >>> import os
    >>> os.chdir("/")
    >>> os.getcwd()
    '/'
    >>> with chdir("/tmp"):
    ...     assert os.getcwd() == "/tmp"
    ...
    >>> assert os.getcwd() == "/"
    """
    cwd = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(cwd)


def check_executable(executable):
    """Checks if an executable exists, logs and exits otherwise."""
    if shutil.which(executable) is None:
        print(f"{executable} is not in the PATH.", file=sys.stderr)
        sys.exit(1)


def run(args):
    """Wrapper for subprocess.run."""
    return subprocess.run(  # nosec
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        check=False,
    )


def check_file(args, file=None):
    """A simple check for a file, may be used to build more complex checks."""
    proc = run(args)
    if proc.returncode > 0:
        if file is not None:
            print(f"In file {file}:")
        print(proc.stdout)
    return proc.returncode


def check_directory(args, directory):
    "A simple check for a directory, may be used to build more complex checks."
    with chdir(directory):
        proc = run(args)
        if proc.returncode > 0:
            print(f"In {directory}:")
            print(proc.stdout)
        return proc.returncode


def bulk_check(checker, items):
    """Bulk check files.

    Some programs can only accept a single file or directory to process at a
    time. This function receives a function that returns the check function and
    list to go through. The function returns 0 if all checks returned 0 or 1
    otherwise.
    """
    returncode = 0
    for item in items:
        check = checker(item)
        if check > 0:
            returncode = 1
    return returncode
