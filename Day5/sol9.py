# Challenge 9: Write a Python program that creates a user in Linux using subprocess and verifies the creation.

import subprocess


def create_user(username):
    try:
       
        # Use subprocess to create a user
        subprocess.run(['sudo', 'useradd', '-m', '-s', '/bin/bash', username], check=True)
        print(f"User '{username}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating user '{username}': {e}")


def verify_user(username):
    try:
        # Check if the user exists
        result = subprocess.run(['id', username], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"User '{username}' exists.")
        else:
            print(f"User '{username}' does not exist.")
    except subprocess.CalledProcessError as e:
        print(f"Error verifying user '{username}': {e}")


username = input("Enter the username to create: ")
create_user(username)
verify_user(username)