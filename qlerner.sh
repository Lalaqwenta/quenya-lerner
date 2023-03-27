#!/bin/bash

# Check if Docker is installed
if ! command -v docker &> /dev/null
then
    echo "Docker not found. Installing Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    rm -f get-docker.sh
fi

# Pull the Docker image
docker pull lalaqwenta/quenya-lerner

# Run the Docker container
./start.sh

# Open browser
xdg-open http://localhost:5000
