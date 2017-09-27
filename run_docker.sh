#!/bin/sh

docker stop ht4_db
docker rm ht4_db
docker rmi ht4_db
docker build . -t ht4_db 
docker run -d --name ht4_db --net=host ht4_db python3 /code/dbapi/manage.py runserver 0.0.0.0:8003