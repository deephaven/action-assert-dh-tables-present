#!/bin/sh

docker build --tag deephaven-examples/validate-tables /github-actions-validate/
TABLE_NAMES=$1 HOST=$2 docker-compose -f /github-actions-validate/docker-compose.yml -p $3 up --exit-code-from validate-tables
