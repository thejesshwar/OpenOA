#!/usr/bin/env bash
# Exit on error
set -o errexit

# 1. Install the missing tool manually
pip install "setuptools<70.0.0" wheel

# 2. Now install the rest of the libraries
pip install -r requirements.txt