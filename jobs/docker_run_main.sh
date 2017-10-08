#!/bin/sh

docker stop ht4_mic_db
docker rm ht4_mic_db
docker run -d --name=ht4_mic_db --net=host ht4_mic_db python3 /code/dbapi/manage.py runserver 0.0.0.0:8003