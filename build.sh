#!/usr/bin/env bash
# Exit on error
set -o errexit

# Upgrade build tools to handle modern library packaging
pip install --upgrade pip setuptools wheel

# Install dependencies
pip install -r requirements.txt