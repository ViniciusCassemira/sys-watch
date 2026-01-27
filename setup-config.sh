#!/bin/bash
set -e

if [ ! -d /etc/systemd/system ]; then
    echo "Error to find /etc/systemd/system"
    exit 1
fi

# Copy service and timer files to systemd directory
cp ./sys_watch.service /etc/systemd/system/sys_watch.service
cp ./sys_watch.timer /etc/systemd/system/sys_watch.timer

# Reload systemd to recognize new service and timer
sudo systemctl daemon-reload
echo "Service and timer have been set up successfully."
echo "You can start the timer with: sudo systemctl start sys_watch.timer"
