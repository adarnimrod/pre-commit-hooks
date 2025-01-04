"""Validate Terraform modules."""

import argparse
import os
import pathlib
import sys
import hooks.utils


TF_CLI = os.getenv("TF_CLI", "terraform")


def tf_validate(directory):  # noqa: D213
    """Validate Terraform modules.

    Also runs init -backend=false to install the providers.
    """
    if (
        hooks.utils.check_directory(
            [TF_CLI, "init", "-backend=false"], directory=directory
        )
        > 0
    ):
        return 1
    if (
        hooks.utils.check_directory([TF_CLI, "validate"], directory=directory)
        > 0
    ):
        return 1

    return 0


def main():
    """Main entrypoint."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="+", type=pathlib.Path)
    args = parser.parse_args()
    hooks.utils.check_executable(TF_CLI)
    os.putenv("TF_INPUT", "0")
    os.putenv("TF_IN_AUTOMATION", "1")
    return hooks.utils.bulk_check(
        tf_validate, hooks.utils.unique_directories(args.file)
    )


if __name__ == "__main__":
    sys.exit(main())
