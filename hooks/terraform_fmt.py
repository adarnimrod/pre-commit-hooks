"""Format Terraform modules."""

import argparse
import os
import pathlib
import sys
import hooks.utils


TF_CLI = os.getenv("TF_CLI", "terraform")


def main():
    """Main entrypoint."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="+", type=pathlib.Path)
    args = parser.parse_args()
    hooks.utils.check_executable(TF_CLI)
    os.putenv("TF_INPUT", "0")
    os.putenv("TF_IN_AUTOMATION", "1")
    return hooks.utils.bulk_check(
        lambda x: hooks.utils.check_file([TF_CLI, "fmt", "-diff", x]),
        hooks.utils.unique_directories(args.file),
    )


if __name__ == "__main__":
    sys.exit(main())
