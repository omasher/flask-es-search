#!/bin/sh

set -e

ES_HOST="$1"

timeout 300 bash -c "until curl --silent --output /dev/null $ES_HOST/_cat/health?h=st; do printf '.'; sleep 5; done; printf '\n'"

python run.py

exec "$@"