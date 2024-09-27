#!/usr/bin/env bash

# Examples:
#   - ./utils/tests/activity_outcome.sh $TEST_PROJECT_DEFAULT_BRANCH push state complete "first_push"
#   - ./utils/tests/activity_outcome.sh $TEST_PROJECT_STAGING_ENV environment.resources.update result failure "add_service"

ENVIRONMENT=$1
ACTIVITY_TYPE=$2
PROPERTY=$3
EXPECTED_OUTCOME=$4
STEP_DESCRIPTOR=$5

# Get the activity id.
ACTIVITY_ID=$(upsun activity:list --type $ACTIVITY_TYPE -e $ENVIRONMENT --limit 1 --no-header --columns=id --format plain)

# Get property state value for the activity.
ACTIVITY_STATE=$(upsun activity:get $ACTIVITY_ID -P $PROPERTY)

# Run the test.
echo "::notice::Attempting to retrieve $STEP_DESCRIPTOR activity outcome."
if [ "$ACTIVITY_STATE" != "$EXPECTED_OUTCOME" ]; then
    echo "::error::Unexpected outcome for activity ($STEP_DESCRIPTOR) property '$PROPERTY'."
    echo "::error::Got '$ACTIVITY_STATE', expected '$EXPECTED_OUTCOME'. Exiting."
    exit 1
else
    echo "::notice::Expected outcome for property '$PROPERTY' ($EXPECTED_OUTCOME). Success."
fi
