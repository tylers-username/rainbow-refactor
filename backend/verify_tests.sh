#!/usr/bin/env bash

MAX_HIGH=0
MAX_CRITICAL=0

npm install cross-env npm-run-all -g
npm install

npm run prettier:backend

npm run prettier:frontend

npm run lint:frontend

npm run test:frontend

npm run lint:backend

npm run test:backend

echo "::notice::Checking for high vulnerabilities in frontend Node.js app dependencies."
cd frontend
export CI=true
HIGH_VULN_ALLOWED=$MAX_HIGH
HIGH_VULN=$(npm audit --json | jq '.metadata.vulnerabilities.high')
if [ "$HIGH_VULN" -gt "$HIGH_VULN_ALLOWED" ]; then
    echo "::error::NPM HIGH vulnerabilities exceed allowed budget."
    npm audit
    exit 1
else
    echo "::notice::No HIGH vulnerabilities found on frontend app."
fi


echo "::notice::Checking for critical vulnerabilities in frontend Node.js app dependencies."
export CI=true
CRITICAL_VULN_ALLOWED=$MAX_CRITICAL
CRITICAL_VULN=$(npm audit --json | jq '.metadata.vulnerabilities.high')
if [ "$CRITICAL_VULN" -gt "$CRITICAL_VULN_ALLOWED" ]; then
    echo "::error::NPM CRITICAL vulnerabilities exceed allowed budget."
    npm audit
    exit 1
else
    echo "::notice::No CRITICAL vulnerabilities found on frontend app."
fi
