#!/bin/bash

SERVICE="nginx"

echo "Checking if $SERVICE is installed..."

# Check if Nginx is already installed
if command -v $SERVICE > /dev/null 2>&1; then
    echo "$SERVICE is already installed."
    exit 0
fi

echo "$SERVICE is not installed. Installing..."

# Install Nginx
sudo apt-get update -y
sudo apt-get install -y $SERVICE

# Check installation status
if command -v $SERVICE > /dev/null 2>&1; then
    echo "$SERVICE installation completed successfully!"
    exit 0
else
    echo "❌ Installation failed!"
    exit 1
fi