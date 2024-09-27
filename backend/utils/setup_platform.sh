#!/usr/bin/env bash

DOWNLOAD_LINK="https://docs.platform.sh/administration/cli.html"

if [ -z ${CI+x} ]; then 
    echo "CI is unset"; 
    if ! command -v platform &> /dev/null; then
        printf "

Requirement - platform: Not found

\033[1m"ERROR"\033[0m

The Platform.sh CLI was not found, and is required to build this project locally.

Visit $DOWNLOAD_LINK to download, then try again.

"
        exit 1
    else 
        RECOMMENDED_VERSION=$(npm pkg get 'otherDependencies.platform' | tr -d '\"')
        CURRENT_VERSION=$(platform -V)
        CURRENT_VERSION=${CURRENT_VERSION:16}
        printf "

Requirement - platform: Installed
* Installed:    $CURRENT_VERSION
* Recommended:  $RECOMMENDED_VERSION

If your intalled version doesn't match what this demo has been made for, check the link below for instructions
to update.

$DOWNLOAD_LINK
"
    fi

else 
    echo "CI is set to '$CI'"; 
fi
