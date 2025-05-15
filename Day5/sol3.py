# Challenge 3: Create a Python script that generates a random password 

import secrets
import string

def generate_password(length):
    if length < 8:
        print("Password length must be at least 8 ")
        return None 
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

length = (int)(input("Enter the length of the password (min 8): \n"))
password = generate_password(length)
if password:
    print(f"Generated password: {password}")