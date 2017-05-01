#!/usr/bin/env bash

# one or the other - python3 or 2
python3 -m venv --clear venv
# virtualenv --clear venv

venv/bin/pip install -U pip
venv/bin/pip install -U setuptools
venv/bin/pip install -U -r requirements.txt
