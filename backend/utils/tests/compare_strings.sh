#!/usr/bin/env bash

# Examples:
#   - ./utils/tests/compare_strings [RESULT_STRING] [EXPECTED_STRING] [JOB_DESCRIPTOR]

RESULT_STRING=$1
EXPECTED_STRING=$2
JOB_DESCRIPTOR=$3

if [ "$RESULT_STRING" != "$EXPECTED_STRING" ]; then
    echo "::error::$JOB_DESCRIPTOR was not successful."
    echo "::error::Got '$RESULT_STRING', expected '$EXPECTED_STRING'. Exiting."
    exit 1
else
    echo "::notice::$JOB_DESCRIPTOR was successful ($RESULT_STRING)."
fi
