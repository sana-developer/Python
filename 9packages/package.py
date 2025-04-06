"""
2️⃣ What is a Package?
A package is a folder that contains multiple modules and a special __init__.py file to indicate it's a package.

✅ Example: Creating a Package
📌 Folder Structure

my_project/
 ├── mypackage/  (This is a package)
 │   ├── __init__.py  (Makes it a package)
 │   ├── math_utils.py  (A module inside the package)
 │   ├── string_utils.py  (Another module inside the package)
 ├── main.py  (Main script)

# 📌 Step 1: Create math_utils.py inside mypackage/
"""
# mypackage/math_utils.py
def multiply(a, b):
    return a * b
# 📌 Step 2: Create __init__.py inside mypackage/

# mypackage/__init__.py
from .math_utils import multiply  # Import function into package

# 📌 Step 3: Use the Package in main.py


from mypackage import multiply

print(multiply(4, 5))  # Output: 20

# ✅ Now, the package groups related modules together, making the project more manageable.

"""
📌 When to Use Modules vs. Packages
Feature	Module (file.py)	Package (folder/)
Use Case	Small scripts	Large projects with multiple related modules
Example	math_utils.py	mypackage/ with multiple modules
Import Method	import module	from package import module
"""