#!/usr/bin/env bash

# 1. Install project dependencies
npm install
# 2. Run backend Python app tests (check for vulnerabilities)
npm run test:backend
# 3. Run frontend React tests.
npm run test:frontend -- --watchAll
# 4. Audit frontend dependencies.
cd frontend && npm audit
# 5. Prettier.
cd ..
npm run prettier:backend
npm run prettier:frontend
npm run lint:frontend
npm run lint:backend
