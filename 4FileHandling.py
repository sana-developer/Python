"""
File Handling
1. Reading and Writing Files
Python allows you to work with files using the open() function.

Basic Modes:
r: Read mode (default).

w: Write mode (creates a new file or overwrites an existing file).

a: Append mode (adds to the file without deleting existing content).
"""	

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, Sana!\n")  # Write content to the file.
    file.write("Welcome to Python file handling.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()  # Read the entire content of the file.
    print(content)

"""
Challenge 1: Write and Read
Write a program that:
Prompts the user to enter their name and age.
Writes this data to a file named user_data.txt.
Reads the file content and displays it.
"""
name = str(input("Enter Your Name: "))
age = int(input("Enter your Age: "))

with open("user_data.txt","w") as file:
    file.write(f"User Name is: {name} and Age is {age}")

with open("user_data.txt","r") as file:
    content=file.read()
    print(content)

"""
2. Error Handling with Files
You can combine file handling with error handling to manage issues like missing files.
"""

try:
    # Attempt to open a non-existent file
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")
finally:
    print("File operation completed.")


"""
Challenge 2: Error Handling with Files
Write a program that:
Prompts the user to enter a file name.
Tries to open and read the file.
Handles the case where the file does not exist.
"""
fileName = input("Enter a file name: ")

try:
    with open(fileName,"r") as file:
        content=file.read()
        print(content) 

except FileNotFoundError:
    print("Error: file not found...")

finally:
    print("execution completed")


#append a file
with open("user_data.txt","a") as file:
    file.write("\nThis is an appended line.")
    