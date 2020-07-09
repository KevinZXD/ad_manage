#!/bin/bash
ps -ef|grep "uwsgi"|grep $1|grep "supervisor"|grep -v "stop_uwsgi"|grep -v "grep"|awk '{print $2}'|xargs kill -9
count=0
let max_count=0
host=$(hostname)
while [ 1 ]; do
    echo "stop_uwsgi.sh already sleep: $count seconds on host: $host, max wait time: $max_count"
    PROCESS_NUM=$(ps -ef|grep "uwsgi"|grep $1|grep -v "stop_uwsgi"|grep -v "grep"| wc -l)
    if [ $PROCESS_NUM -eq 0 ]; then
        exit 0
    fi

    if [ $count -ge $max_count ]; then
        ps -ef|grep "uwsgi"|grep $1|grep -v "stop_uwsgi"|grep -v "grep"|awk '{print $2}'|xargs kill -9
        exit 0
    fi

    ps -ef|grep "uwsgi"|grep $1|grep -v "stop_uwsgi"|grep -v "grep"|awk '{print $2}'|xargs kill -15
    sleep 3
    let count+=3
done