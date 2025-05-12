#!/bin/bash

# Write a script that takes a filename as an argument, checks if it exists, and
#  prints the content of the file accordingly.

if [ $# -eq 0 ]; then
	echo "Provide the filename as argument"
	exit 1
fi

FILENAME="$1"

if [ -f $FILENAME ]; then
	echo "$FILENAME found, the content in file is "
	cat $FILENAME
else
	echo "$FILENAME not found"
fi

