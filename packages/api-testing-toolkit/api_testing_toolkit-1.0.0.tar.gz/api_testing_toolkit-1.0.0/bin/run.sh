#!/usr/bin/env bash

set -e

source ./.env/bin/activate

jupyter lab ./examples
