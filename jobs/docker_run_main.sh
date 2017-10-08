#!/bin/sh

docker run -d --name=ht4_db --net=host ht4_db python3 /code/dbapi/manage.py runserver 0.0.0.0:8003