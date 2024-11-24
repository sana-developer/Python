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