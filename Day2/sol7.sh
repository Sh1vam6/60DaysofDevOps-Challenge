#!/bin/bash

# Write a script that automatically deletes log files older than 7 days from /var/log.


LOG_DIR="/var/log"

DAYS=7

find "$LOG_DIR" -type f -name "*.log" -mtime +$DAYS -exec rm -f {} \;

