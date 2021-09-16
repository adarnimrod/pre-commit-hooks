# pre-commit hooks

A collection of [pre-commit](https://pre-commit.com/) hooks.

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
    - id: terraform-fmt  # uses the installed system terraform.
    - id: terraform-validate  # uses the installed system terraform.
    - id: poetry-check
    - id: branch-merge-conflict
    - id: pip-outdated
```

## License

This software is licensed under the MIT license (see `LICENSE.txt`).

## Author Information

Nimrod Adar, [contact me](mailto:nimrod@shore.co.il) or visit my
[website](https://www.shore.co.il/). Patches are welcome via
[`git send-email`](http://git-scm.com/book/en/v2/Git-Commands-Email). The repository
is located at: <https://git.shore.co.il/explore/>.
