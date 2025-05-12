#!/bin/bash

# Create a script that monitors CPU and memory usage every 5 seconds and logs the results to a file.


LOG_FILE="resource_usage.log"

echo "Timestamp | CPU (%) | Memory (%)" > "$LOG_FILE"

while true; do
	TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

	#cpu usage
	CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
        
	#memory usage
	MEM_USAGE=$(free | awk '/Mem/ {printf "%.2f", $3/$2 * 100}')
 
	echo "$TIMESTAMP | $CPU_USAGE | $MEM_USAGE" >> "$LOG_FILE"

	#wait for 10 sec
	sleep 10
done

# Run the script in the background:nohup ./sol6.sh &
# nohup → Keeps the script running even if you log out.& → Runs it in the background.
