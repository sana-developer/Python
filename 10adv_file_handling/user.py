# r for reading, w for writing, a for appending, r+ for both reading and writing

# 📌 Lesson: File Handling in Python
# Python allows you to read, write, and manipulate files using built-in functions.

# 1️⃣ Opening a File

file = open("example.txt", "r")  # "r" means read mode
content = file.read()
print(content)
file.close()  # Always close the file after use!

# ✅ Best Practice: Instead of manually closing a file, use with open():

with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # File automatically closes after this block

# 2️⃣ Writing to a File

with open("example.txt", "w") as file:
    file.write("Hello, Sana!\nWelcome to file handling.")

# ✅ "w" mode overwrites the file.
# ✅ Use "a" mode to append data:

with open("example.txt", "a") as file:
    file.write("\nThis is a new line added!")

# 3️⃣ Reading a File Line by Line

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # `strip()` removes newline characters

# 4️⃣ Working with Binary Files (e.g., Images, PDFs)

with open("image.jpg", "rb") as file:  # "rb" = read binary
    binary_data = file.read()

# ✅ "wb" mode is used for writing binary files.



with open("user_data.txt","r") as file:
    for line in file:
        print(line.strip())  # `strip()` removes newline characters


#asking user for input
name = input("Enter your name:")
with open("user_data.txt","a") as file:
    file.write(name)


def copy_file(src, dest):
    with open(src,"r") as file:
        content = file.read()
        with open(dest,"w") as file:
            file.write(content)

copy_file("user_data.txt","new.txt")