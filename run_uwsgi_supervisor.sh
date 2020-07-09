#!/bin/bash
start_uwsgi_server() {
    (./run_uwsgi.sh $1)
}

TARGET_NUMBER=1
while [ 1 ]; do
    DOG_NUMBER=$(ps -ef | grep "run_uwsgi.sh $1\|0.0.0.0:$1" | grep -v "grep" | wc -l)
    if [ $DOG_NUMBER -lt $TARGET_NUMBER ]; then
        echo "$(date +%Y-%m-%d\ %H:%M:%S) increase uwsgi server number to $TARGET_NUMBER"
        start_uwsgi_server $1
    else
        sleep 10
    fi
    TIME_SUM=$((10#`date +%H%M%S`))
    if [ $TIME_SUM -lt 10 ]; then
        kill -SIGHUP $(cat uwsgi-$1.pid)
    fi
done