#!/usr/bin/env bash

python3 -m venv --system-site-packages .venv
. .venv/bin/activate
pip install -r solid-fenics/requirements.txt
