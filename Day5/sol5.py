 # Challenge 5: Write a script that reads a list of server names from a file and pings each one.

import os 
import platform

def ping_server(server):
    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    response = os.system(f"ping {param} {server} > /dev/null 2>&1")
    return response == 0


try:
    file_name = input("Enter the file name containing server names: \n")

    with open(file_name, 'r') as file:
        servers = [line.strip() for line in file.readlines()]
    
    for server in servers:
        if server:
            status = "Reachable" if ping_server(server) else "Unreachable"
            print(f"{server} : {status}.")

except FileNotFoundError:
    print(f"The file {file_name} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")