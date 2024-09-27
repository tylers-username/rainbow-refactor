#!/usr/bin/env bash

# Examples:
#   - ./utils/tests/command_installed.sh upsun

COMMAND=$1

if ! [ -x "$(command -v $COMMAND)" ]; then
    echo "::error::'$COMMAND' is not installed and/or not executable. Exiting." >&2
    exit 1
else
    echo "::notice::'$COMMAND' is installed and executable. Success."
fi
