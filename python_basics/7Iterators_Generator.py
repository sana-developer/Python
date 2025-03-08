#these concepts are useful when dealing with large dataset

# An iterator is an object that lets you loop through a sequence one item at a time without storing the entire sequence in memory.
# An iterator is an object that remembers its current position and returns items one by one when we call next().

class EvenNumbers:
    def __init__(self,max_num):
        self.num = 0
        self.max_num = max_num
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= self.max_num:
            result = self.num
            self.num +=2
            return result
        else:
            raise StopIteration

# Create an object of the EvenNumbers class
even_numbers = EvenNumbers(10)

for num in even_numbers:
    print(num)

# Generators are a simple way to create iterators using functions. You can also use a generator expression to create a generator object.
# A generator is a special type of function that remembers its state and generates values one at a time using yield instead of return.

def fibonacci(max_num):
    a,b = 0,1
    for _ in range(1,max_num+1):
        yield a
        a,b = b , a+b

for num in fibonacci(10):
    print(num)