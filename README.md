# Python Programming - Core Concepts

This repository contains Python code that demonstrates essential programming concepts, including variables, conditionals, loops, functions, data structures (lists, tuples, dictionaries, sets), error handling, file handling, and object-oriented programming (OOP).

## Features:
- **Basic Python Syntax:** Demonstrates how to use variables, conditionals, loops, and functions in Python.
- **Data Structures:** Provides examples of Python's built-in data structures such as lists, tuples, dictionaries, and sets.
- **Error Handling:** Implements error handling using try-except blocks to catch common errors like division by zero or invalid input.
- **Functions with Arguments:** Includes examples of functions with default arguments, variable-length arguments (*args), and keyword arguments (**kwargs).
- **File Handling:** Shows how to read from and write to files in Python.
- **Object-Oriented Programming (OOP):** Includes simple examples of classes and objects, inheritance, and encapsulation.

## Code Overview:
The following sections demonstrate key concepts in Python:

### 1. **Variables & Output**
```python
name = "Sana"
age = 21
print(f"My name is {name} and I am {age} years old.")


2. Conditionals
python
Copy code
if age >= 18:
    print("You're an adult.")
else:
    print("You're young.")


3. Loops
For Loop:
python
Copy code
for num in [1, 2, 3, 4, 5]:
    print(f"number: {num}")
While Loop:
python
Copy code
count = 4
while count > 0:
    print("we are in while loop")
    count -= 1


4. Functions
python
Copy code
def newfunc(name):
    return f"hii, {name}!"


5. Data Structures
List:
python
Copy code
fruits = ["apple", "banana", "grapes"]
Tuple:
python
Copy code
dimensions = (1400, 3489)
Dictionary:
python
Copy code
student = {"name": "Sana", "age": 21, "skills": ["C++", "Python"]}
Set:
python
Copy code
numbers = {1, 2, 3, 4}


6. Error Handling
python
Copy code
try:
    result = int(input("Enter a number: ")) / int(input("Enter another number: "))
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter valid integers.")


7. Object-Oriented Programming (OOP)
python
Copy code
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Sana", 21)
person1.display()


Challenges:
This repository also includes challenges that involve working with lists, tuples, dictionaries, sets, functions, and error handling. Each challenge is designed to improve your Python skills.

How to Run:
Clone this repository to your local machine.
Navigate to the directory where the code is saved.
Run the Python script using the command:
bash
Copy code
python <script_name>.py
License:
This project is open-source and available under the MIT License.

yaml
Copy code

---

Feel free to add your GitHub URL for the repository at the top of the README file if you'd like! This structure provides a clean overview of your code and its functionality.