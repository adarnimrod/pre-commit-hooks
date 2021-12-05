"""Fix known backwards incompatibilities in Packer templates."""

import argparse
import locale
import pathlib
import sys
import hooks.utils


def packer_fix(file):
    """Runs packer fix.

    If the invocation succeeds, overwrite the file with the fixed output from
    packer. If it fails, fail.
    """
    proc = hooks.utils.run(["packer", "fix", file])
    if proc.returncode > 0:
        return 1
    # pylint: disable=invalid-name
    with open(file, "w", encoding=locale.getpreferredencoding()) as fh:
        fh.write(proc.stdout)
    return 0


def main():
    """Main entrypoint."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="+", type=pathlib.Path)
    args = parser.parse_args()
    hooks.utils.check_executable("packer")
    return hooks.utils.bulk_check(
        packer_fix,
        args.file,
    )


if __name__ == "__main__":
    sys.exit(main())
