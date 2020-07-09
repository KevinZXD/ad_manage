#!/bin/bash
nohup ./run_uwsgi_supervisor.sh $1 >uwsgi_dog-$1.log 2>&1 &