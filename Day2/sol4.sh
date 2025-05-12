#!/bin/bash

# Create a script that lists all running processes and writes the output to a file named process_list.txt.

OUTPUT_FILE="process_list.txt"

ps aux > $OUTPUT_FILE
