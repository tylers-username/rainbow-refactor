#!/usr/bin/env bash

# Install dependencies
poetry install

# Run pip-audit within the Poetry environment
poetry run pip-audit