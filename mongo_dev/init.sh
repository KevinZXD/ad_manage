mongod --fork --logpath /tmp/mongo.log ;mongo /data/db/init.js;ps -elf|grep mongod|grep -v grep|awk '{print $4}'|xargs kill -9;mongod --auth
