#!/usr/bin/env bash

# Install dependencies
poetry install

# Run pylint within the Poetry environment
poetry run pylint main.py app/**/*.py