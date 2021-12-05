"""Rewrites all Packer configuration files to a canonical format."""

import argparse
import pathlib
import sys
import hooks.utils


def main():
    """Main entrypoint."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="+", type=pathlib.Path)
    args = parser.parse_args()
    hooks.utils.check_executable("packer")
    return hooks.utils.bulk_check(
        lambda x: hooks.utils.check_file(["packer", "fmt", "-diff", x]),
        args.file,
    )


if __name__ == "__main__":
    sys.exit(main())
