"""Checks that the Packer template is valid."""

import argparse
import pathlib
import sys
import hooks.utils


def packer_validate(file):
    """Validate a Packer template.

    Run init when needed.
    """
    if str(file).endswith(".pkr.hcl") or str(file).endswith(".pkr.json"):
        if hooks.utils.check_file(["packer", "init", file]) > 0:
            return 1
    return hooks.utils.check_file(["packer", "validate", file])


def main():
    """Main entrypoint."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="+", type=pathlib.Path)
    args = parser.parse_args()
    hooks.utils.check_executable("packer")
    return hooks.utils.bulk_check(
        packer_validate,
        args.file,
    )


if __name__ == "__main__":
    sys.exit(main())
