#!/bin/sh

docker stop ht4_mic_db
docker rm ht4_mic_db
docker rmi ht4_mic_db
docker build . -t ht4_mic_db 