# pre-commit hooks

A collection of [pre-commit](https://pre-commit.com/) hooks.

## Requirements

- Supported Python 3 version (at time of writing 3.6 or later).
- [pre-commmit](https://pre-commit.com/) 2.0.0 or later.
- [Terraform](https://www.terraform.io/) (for the terraform hooks).

## Example .pre-commit-config.yaml

```yaml
---
- repo: https://git.shore.co.il/nimrod/pre-commit-hooks.git
  rev: 0.1.0  # Check for the latest tag or run pre-commit autoupdate.
  hooks:
    - id: shell-validate
    - id: ansible-syntax-check
    - id: ansible-vault-check
    - id: docker-compose
    - id: terraform-fmt
    - id: terraform-validate
    - id: poetry-check
    - id: branch-merge-conflict
    - id: pip-outdated
```

## Available hooks

### `shell-validate`

Check shell scripts with `/bin/sh -en`.

### `ansible-syntax-check`

Check Ansible playbooks for syntax errors.

### `ansible-vault-check`

Verify that Ansible Vault files are vaulted.

### `docker-compose`

Validate the Docker Compose file using docker-compose config.

### `terraform-fmt`

Format Terraform files using `terraform fmt`.
Requires an installed `terraform`.

### `terraform-validate`

Validate Terraform modules using `terraform validate`.
Requires an installed `terraform`.

### `poetry-check`

Validate `pyproject.toml` files using Poetry.

### `branch-merge-conflict`

Checks for merge conflicts with a specific branch.

### `pip-outdated`

Find outdated Python dependencies in your requirements files.

## License

This software is licensed under the MIT license (see `LICENSE.txt`).

## Author Information

Nimrod Adar, [contact me](mailto:nimrod@shore.co.il) or visit my
[website](https://www.shore.co.il/). Patches are welcome via
[`git send-email`](http://git-scm.com/book/en/v2/Git-Commands-Email). The repository
is located at: <https://git.shore.co.il/explore/>.
