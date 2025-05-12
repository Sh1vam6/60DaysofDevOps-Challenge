#!/bin/bash


# Use awk or sed in a script to process a log file and extract only error messages.


LOG_FILE="/var/log/alternatives.log.1"
OUTPUT_FILE="error.log"


if [ ! -f $LOG_FILE ]; then
	echo "log file doesn't exist"
	exit 1
fi

# extract error message
awk '/error|ERROR|Error/ {print}' $LOG_FILE > $OUTPUT_FILE

# using sed command
# sed -n '/error\|ERROR\|Error/p' "$LOG_FILE" > "$OUTPUT_FILE"

