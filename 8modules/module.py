"""	
1️⃣ What is a Module?
A module is just a Python file (.py) that contains functions, classes, or variables.

✅ Example: Creating a Module
📌 Step 1: Create a Python file math_utils.py
"""

# math_utils.py (a module)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# 📌 Step 2: Import and Use the Module


import math_utils

print(math_utils.add(5, 3))  # Output: 8
print(math_utils.subtract(10, 4))  # Output: 6

# This helps keep functions organized in separate files instead of writing everything in one file.

