#!/bin/bash

echo "Stopping existing containers..."
docker-compose down -v

echo "Building the backend service..."
docker-compose build --no-cache

echo "Starting the backend service..."
docker-compose up -d