#!/bin/bash

# Create a script that checks if a website (e.g., https://www.learnxops.com) is reachable using curl or ping.
#  Print a success or failure message.

WEBSITE="https://www.learnxops.com"
DOMAIN="learnxops.com"

if curl -Is "$WEBSITE" --max-time 5 | head -n 1 | grep -q "200\|301\|302"; then
	echo " Success, $WEBSITE is reachable via curl"
else
	echo " Failure, Now trying ping"

	if ping -c 2 -W 2 "$DOMAIN" > /dev/null 2>&1; then
		echo "Success, $DOMAIN is reachable via ping"
	else 
		echo "Failure, Not reachable by both ping and curl"
	fi
fi









