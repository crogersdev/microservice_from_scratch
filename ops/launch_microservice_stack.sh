#!/bin/bash

docker-compose up &
wait
bash -x ../db/bootstrap_foo_db.sh