#!/bin/sh

while ! nc -z elasticsearch 9200; do 
    sleep 1
    echo "Waiting on Elasticsearch to launch on 9200..."
done

echo "Elasticsearch is running"

python run.py

exec "$@"