# Challenge 8: Create a Python script that monitors CPU and memory usage every few seconds.

import psutil 
import time 

def monitor_resources(interval):
    while True:
        cpu_usage = psutil.cpu_percent(interval)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")

        
try:    
    interval = int(input("Enter the monitoring interval in seconds: "))
    if interval <= 0:
        raise ValueError("Interval must be a positive integer.")
    monitor_resources(interval)
except ValueError as e:
    print(f"Invalid input: {e}")