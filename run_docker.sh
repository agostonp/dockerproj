#!/usr/bin/env bash

# Build docker image
docker build --tag=demolocal .

#List images
docker image ls

#Open shell inside docker image
docker run -it demolocal bash