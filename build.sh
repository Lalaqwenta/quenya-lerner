#!/bin/bash

# if [[ "$1" == "--develop=true" ]]; then
    DOCKERFILE=Dockerfile.dev
# else
#     DOCKERFILE=Dockerfile.prod
# fi

# Build Docker image
docker build -t lalaqwenta/quenya-lerner -f $DOCKERFILE .
