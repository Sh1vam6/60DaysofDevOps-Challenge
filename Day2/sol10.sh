#!/bin/bash

# Define backup directory and destination
SOURCE_DIR="/path/to/directory"   
BACKUP_DIR="/path/to/backup"

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/backup_$TIMESTAMP.tar.gz"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Create the backup archive
tar -czf "$BACKUP_FILE" "$SOURCE_DIR"

#Schedule a Daily Cron Job:
#crontab -e
#Add the following line to run the script daily at 2 AM:0 2 * * * /path/to/sol10.sh >> /var/log/backup.log 2>&1
#Verify by  crontab -l
