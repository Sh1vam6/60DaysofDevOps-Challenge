# Challenge 7: Automate a simple task using Python (e.g., renaming multiple files in a directory).

import os 

directory = input("Enter the directory path: \n")
prefix = input("Enter the prefix to add to each file: \n")



try:
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            new_name = prefix + filename
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f"Renamed {filename} to {new_name}")
            
except FileNotFoundError:
    print(f"The directory {directory} does not exist.")
except PermissionError:
    print(f"Permission denied to rename files in {directory}.")
except Exception as e:
    print(f"An error occurred: {e}")