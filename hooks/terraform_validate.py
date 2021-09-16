"""Validate Terraform modules."""

import argparse
import os
import pathlib
import sys
import hooks.utils


def checker():
    def check(directory):
        if (
            hooks.utils.check(
                ["terraform", "init", "-backend=false"], directory=directory
            )
            > 0
        ):
            return 1
        if (
            hooks.utils.check(["terraform", "validate"], directory=directory)
            > 0
        ):
            return 1

        return 0

    return check


def main():
    """Main entrypoint."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="+", type=pathlib.Path)
    args = parser.parse_args()
    hooks.utils.check_executable("terraform")
    os.putenv("TF_INPUT", "0")
    os.putenv("TF_IN_AUTOMATION", "1")
    return hooks.utils.bulk_check(
        checker, hooks.utils.unique_directories(args.file)
    )


if __name__ == "__main__":
    sys.exit(main())
