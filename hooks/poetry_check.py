"""Validate Docker Compose files."""

import argparse
import pathlib
import sys
import hooks.utils


def main():
    """Main entrypoint."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="+", type=pathlib.Path)
    args = parser.parse_args()
    hooks.utils.check_executable("poetry")
    return hooks.utils.bulk_check(
        lambda x: hooks.utils.check_dir(["poetry", "check"], dir=x),
        hooks.utils.unique_directories(args.file),
    )


if __name__ == "__main__":
    sys.exit(main())
