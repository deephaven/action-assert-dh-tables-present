#!/bin/sh

docker build --tag deephaven-examples/assert-tables /assert-tables/
TABLE_NAMES=$1 HOST=$2 MAX_RETRIES=$4 docker-compose -f /assert-tables/docker-compose.yml -p $3 up --exit-code-from assert-tables
