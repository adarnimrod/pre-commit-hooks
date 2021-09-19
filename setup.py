from setuptools import setup, find_packages

with open("VERSION", "r", encoding="utf-8") as fh:
    VERSION = fh.read().strip()

setup(
    name="shore-co-il-pre-commit-hooks",
    url="https://git.shore.co.il/nimrod/pre-commit-hooks",
    author="Nimrod Adar",
    author_email="nimrod@shore.co.il",
    version=VERSION,
    install_requires=[
        "ansible>=4",
        "docker-compose>=1.20",
        "poetry",
    ],
    entry_points={
        "console_scripts": [
            "docker-compose-validate=hooks.docker_compose_validate:main",
            "terraform-validate=hooks.terraform_validate:main",
            "terraform-fmt=hooks.terraform_fmt:main",
            "poetry-check=hooks.poetry_check:main",
        ]
    },
    packages=find_packages(),
)
