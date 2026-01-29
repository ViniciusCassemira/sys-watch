#!/bin/bash
set -e

# Check if systemd directory exists
if [ ! -d /etc/systemd/system ]; then
    echo "Error: /etc/systemd/system directory not found." >> ./data/logs.txt
    echo "Error to find /etc/systemd/system"
    exit 1
fi

# Check if unit_files directory and files exist
if [ ! -d ./unit_files ]; then
    echo "Error: unit_files directory not found" >> ./data/logs.txt
    echo "Error to find unit_files directory"
    exit 1
fi

# Check if service and timer files exist
if [ ! -f ./unit_files/sys_watch.service ]; then
    echo "Error: service file not found in unit_files directory." >> ./data/logs.txt
    echo "Error to find service file in unit_files directory"
    exit 1
fi
if [ ! -f ./unit_files/sys_watch.timer ]; then
    echo "Error: timer file not found in unit_files directory." >> ./data/logs.txt
    echo "Error to find timer file in unit_files directory"
    exit 1
fi

# Copy service and timer files to systemd directory
cp ./unit_files/sys_watch.service /etc/systemd/system/sys_watch.service
cp ./unit_files/sys_watch.timer /etc/systemd/system/sys_watch.timer

# Reload systemd to recognize new service and timer
sudo systemctl daemon-reload
echo "- Service and timer have been set up successfully."
echo "- You can start the timer with: sudo systemctl start sys_watch.timer"
