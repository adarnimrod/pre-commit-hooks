# pre-commit hooks

[![pipeline status](https://git.shore.co.il/nimrod/pre-commit-hooks/badges/main/pipeline.svg)](https://git.shore.co.il/nimrod/pre-commit-hooks/-/commits/main)

A collection of [pre-commit](https://pre-commit.com/) hooks.

## Requirements

- Supported Python 3 version (at time of writing 3.6 or later).
- [pre-commmit](https://pre-commit.com/) 2.0.0 or later.

## Optional requirements

- [Terraform](https://www.terraform.io/) or [OpenTofu](https://opentofu.org/)
  (for the `terraform-*` hooks).
- [Packer](https://www.packer.io/) (for the `packer-*` hooks).
- [Docker Compose](https://docs.docker.com/compose/) (for the `docker-compose`
  hook).

## Example .pre-commit-config.yaml

```yaml
---
- repo: https://git.shore.co.il/nimrod/pre-commit-hooks.git
  rev: 0.1.0  # Check for the latest tag or run pre-commit autoupdate.
  hooks:
    - id: shell-validate
    - id: ansible-syntax-check
    - id: docker-compose
    - id: terraform-fmt
    - id: terraform-validate
    - id: packer-fmt
    - id: packer-fix
    - id: packer-validate
    - id: poetry-check
    - id: branch-merge-conflict
```

## Available hooks

### `shell-validate`

Check shell scripts with `/bin/sh -en`.

### `ansible-syntax-check`

Check Ansible playbooks for syntax errors.

### `docker-compose`

Validate the Docker Compose file using docker-compose config.
Requires an install `docker-compose`.

With previous versions of this repo, the `docker-compose` version from PyPI was
installed as a dependency. However, at the time of writing, the package hasn't
been updated in over 3 years. If you wish to still use the 1.x version from
PyPI, add it in the `additional_dependencies` section of the hook.

### `terraform-fmt`

Format Terraform files using `terraform fmt`.
Requires an installed `terraform`. If you wish to use `tofu` instead, set the
`TF_CLI` environment variable to `tofu`.

### `terraform-validate`

Validate Terraform modules using `terraform validate`.
Requires an installed `terraform`. If you wish to use `tofu` instead, set the
`TF_CLI` environment variable to `tofu`.

### `packer-fix`

Fix known backwards incompatibilities in Packer templates (just JSON files,
until support for HCL files is added in Packer).

### `packer-fmt`

Rewrites all Packer configuration files to a canonical format (just HCL files).

### `packer-validate`

Checks that the Packer template is valid.

### `poetry-check`

Validate `pyproject.toml` files using Poetry.

### `branch-merge-conflict`

Checks for merge conflicts with a specific branch.

## License

This software is licensed under the MIT license (see `LICENSE.txt`).

## Author Information

Nimrod Adar, [contact me](mailto:nimrod@shore.co.il) or visit my
[website](https://www.shore.co.il/). Patches are welcome via
[`git send-email`](http://git-scm.com/book/en/v2/Git-Commands-Email). The repository
is located at: <https://git.shore.co.il/explore/>.
