#!/usr/bin/env bash

# NOTE: Run this *before* you start running the IDE.

set -e

python3 -m venv .env
source .env/bin/activate
pip install --upgrade pip
pip install --editable .
