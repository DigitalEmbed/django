#!/bin/bash

#docker run -e POSTGRES_PASSWORD=password
docker run -e POSTGRES_HOST_AUTH_METHOD=trust
sudo chown -R $USER:$USER
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000