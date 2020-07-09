#!/bin/bash
# --post-buffering  enable post buffering
uwsgi --socket=0.0.0.0:$@ --module=conf.wsgi:application --check-static .\
   --enable-threads --master --processes `nproc` \
   --harakiri 60 --harakiri-verbose --max-request 500 --thunder-lock --vacuum  --post-buffering=65536 >>uwsgi-$@.log 2>&1


