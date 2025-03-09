# r for reading, w for writing, a for appending, r+ for both reading and writing

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