#!/bin/bash

LOGFILE="../logs/provisioning.log"

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [BASH] $1" >> "$LOGFILE"
}

log "Nginx installation script started.."

SERVICE="nginx"

echo "Checking if $SERVICE is installed..."

# Check if Nginx is already installed
log "Checking if nginx is installed..."
if command -v $SERVICE > /dev/null 2>&1; then
    echo "$SERVICE is already installed."
    exit 0
fi

echo "$SERVICE is not installed. Installing..."

# Install Nginx
log "Installing nginx service..."
sudo apt-get update -y
echo " Updating apt packages..."
sudo apt-get install -y $SERVICE
echo " Installing $SERVICE..."
log "$SERVICE installation completed."

if command -v $SERVICE > /dev/null 2>&1; then
    echo "$SERVICE installation completed successfully! ✅"
    exit 0
else
    echo "Installation failed! ❌ "
    log "ERROR: Failed to install nginx"
    exit 1
fi

log "Nginx script finished"