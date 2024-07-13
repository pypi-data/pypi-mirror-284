# netrecon
[![PyPi Version](https://img.shields.io/pypi/v/netrecon.svg)](https://pypi.python.org/pypi/netrecon)
[![PyPI Status](https://img.shields.io/pypi/status/netrecon.svg)](https://pypi.python.org/pypi/netrecon)
[![Python Versions](https://img.shields.io/pypi/pyversions/netrecon.svg)](https://pypi.python.org/pypi/netrecon)
[![License](https://img.shields.io/github/license/ReK42/netrecon)](https://github.com/ReK42/netrecon/blob/main/LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/ReK42/netrecon/main?logo=github)](https://github.com/ReK42/netrecon/commits/main)
[![Build Status](https://img.shields.io/github/actions/workflow/status/ReK42/netrecon/build.yml?logo=github)](https://github.com/ReK42/netrecon/actions)
[![Linted by Ruff](https://img.shields.io/badge/linting-ruff-purple?logo=ruff&logoColor=white)](https://github.com/astral-sh/ruff)
[![Code Style by Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A rich CLI tool for network device reconnaissance.

## Installation
Install [Python](https://www.python.org/downloads/), then install `pipx` and use it to install `netrecon`:
```sh
python -m pip install --upgrade pip setuptools pipx
pipx install netrecon
```

## Usage
For all options, run `netrecon --help`

## Development Environment
```sh
git clone https://github.com/ReK42/netrecon.git
cd netrecon
python -m venv .env
source .env/bin/activate
python -m pip install --upgrade pip setuptools pre-commit
pre-commit install
pip install -e .[test]
```
