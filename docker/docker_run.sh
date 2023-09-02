#!/bin/bash

docker run \
  --gpus all \
  --restart always \
  --shm-size=2g \
  -it \
  --name geon-fastAPI_study \
  -p 40001:8888 \
  -p 40002:8000 \
  -p 40003:8080 \
  -v /home/geon/Documents/docker_data/fast_API_study:/home/fast_API_study \
  fast_api:latest

