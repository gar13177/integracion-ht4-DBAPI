#!/bin/sh

docker stop ht4_db
docker rm ht4_db
docker rmi ht4_db
docker build . -t ht4_db 