#List Comprehension : A concise way to create lists

# Practice:
# Try this one:

# Create a list of cubes (numbers raised to the power of 3) for numbers 1 to 5.

cubes = [x**3 for x in range(1,6)]
print(cubes)
# Create a list of odd numbers from 0 to 15.

odd_Num = [x for x in range(0,16) if x%2 != 0]
print(odd_Num)

"""
Functions with arguments
Task 1: Default Arguments
Write a function introduce_yourself that takes a name and an optional age (default is 18). The function should return:
"My name is {name}, and I am {age} years old."
"""
def introduce_yourself(name,age=18):
    return print(f"My name is {name}, and I am {age} years old.")

introduce_yourself("Sana")

"""
*args: variable length arguments(the arguments are collected in a tuple)

Task 2: *args
Write a function multiply_numbers(*args) that multiplies all the numbers passed to it and returns the result.
"""
def multiply_numbers(*args):
    multiply = 1
    for num in args:
        multiply *= num
    return multiply

print(multiply_numbers(1,2,3,4))

"""
**kwargs: variable keyword arguments(the arguments are collected in a dictionary)

'kwargs' is a dictionary where keys are argument names and values are their corresponding values.

Task 3: **kwargs
Write a function student_info(**kwargs) that takes a student's details (like name, age, grade) as keyword arguments and prints them nicely.
"""

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name="Sana",age=21,grade="A",skills=["c++","python"])
"""
Task 4: Error Handling
Write a program that:

Asks the user for two numbers.
Tries to divide the first number by the second.
Catches division by zero errors and non-numeric input errors.
"""
try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = number1/number2
    print(result)

except ValueError:
    print("Error: Please Enter Numeric values only")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

finally:
    print("Execution completed")