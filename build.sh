#!/usr/bin/env bash
# Exit on error
set -o errexit

# 1. Upgrade pip and install setuptools (fixes pkg_resources error)
pip install --upgrade pip setuptools wheel

# 2. Install the requirements
pip install -r requirements.txt