#!/usr/bin/env bash

# Examples:
#   - ./utils/tests/url_status.sh $TEST_PROJECT_PROD_URL_FRONTEND '200' "production frontend deployment"
#   - ./utils/tests/url_status.sh $TEST_PROJECT_STAGING_URL_BACKEND '200' "staging backend deployment"

URL=$1
PROPERTY=$2
EXPECTED_STATUS=$3
URL_DESCRIPTOR=$4

EXPECTED_STATUS="file"
STATUS_DATA=$(curl -s $URL | jq -r '.session_storage')
if [ "$STATUS_DATA" != "$EXPECTED_STATUS" ]; then
    echo "::notice::Backend data session_storage is not the expected value ($EXPECTED_STATUS/$STATUS_DATA). Exiting."
    exit 1
else
    echo "::notice::Backend data session_storage as expected."
fi

EXPECTED_STATUS="production"
STATUS_DATA=$(curl -s $TEST_PROJECT_PROD_URL_BACKEND | jq -r '.type')
if [ "$STATUS_DATA" != "$EXPECTED_STATUS" ]; then
    echo "::notice::Backend data environment type is not the expected value ($EXPECTED_STATUS/$STATUS_DATA). Exiting."
    exit 1
else
    echo "::notice::Backend data environment type as expected."
fi