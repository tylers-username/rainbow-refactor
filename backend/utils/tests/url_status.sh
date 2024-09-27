#!/usr/bin/env bash

# Examples:
#   - ./utils/tests/url_status.sh $TEST_PROJECT_PROD_URL_FRONTEND '200' "production frontend deployment"
#   - ./utils/tests/url_status.sh $TEST_PROJECT_STAGING_URL_BACKEND '200' "staging backend deployment"

URL=$1
EXPECTED_STATUS=$2
URL_DESCRIPTOR=$3
echo "::notice::Testing status for $URL (Expecting $EXPECTED_STATUS)."

STATUS=$(curl --silent --head $URL | awk '/^HTTP/{print $2}')
if [ "$STATUS" != "$EXPECTED_STATUS" ]; then
    echo "::error::Unexpected status for $URL_DESCRIPTOR."
    echo "::error::Got '$STATUS', expected '$EXPECTED_STATUS'. Exiting."
    exit 1
else
    echo "::notice::Expected status for $URL_DESCRIPTOR ($EXPECTED_STATUS). Success."
fi
