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
    hooks.utils.check_executable("docker-compose")
    return hooks.utils.bulk_check(
        lambda x: hooks.utils.check_file(
            ["docker-compose", "--file", x, "config"], file=x
        ),
        args.file,
    )


if __name__ == "__main__":
    sys.exit(main())
