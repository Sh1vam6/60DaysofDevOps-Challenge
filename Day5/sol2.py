# Challenge 2: Write a script that reads a text file and counts the number of words in it.

file_name = input("Enter the file name: \n")

try:
    with open(file_name, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        print(f"The number of words in the file {file_name} is {word_count}.")
except FileNotFoundError:
    print(f"The file {file_name} does not exit")
except Exception as e: 
    print(f"An error occurred: {e}")