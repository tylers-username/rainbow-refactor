#!/usr/bin/env bash

# Install dependencies
poetry install

# Test scenarios 
cp .env.sample .env
