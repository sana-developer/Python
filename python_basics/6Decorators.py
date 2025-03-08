# A decorator is a function that takes another function as input, enhances or modifies it, and returns the modified function.
# Challenge: Build a Custom Decorator
# Task:
# Write a decorator named time_logger that:
# Prints "Start of function".
# Calls the decorated function.
# Prints "End of function".
# Use it to decorate a function process_data() that prints "Processing data...".

def time_logger(func):
    def wrapper():
        print("Start of the function")
        func()
        print("end of the function")
    return wrapper

@time_logger
def process_data():
    print("processing data..")

# call the decorated function
process_data()

# Decorators with arguments
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"function args: {args}, {kwargs}")
        func(*args, **kwargs)
        print("function executed")
    return wrapper

@log_decorator
def add(a, b):
    return a+b

add(2, 3)