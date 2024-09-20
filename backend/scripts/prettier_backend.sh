#!/usr/bin/env bash

# Install dependencies
poetry install

# Make code prettier
poetry run black . --diff --color --check
