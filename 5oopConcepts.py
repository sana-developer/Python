"""
OOP organizes your code into objects and classes, making it reusable and easier to manage.

Class and Object
Self represents the instance of the class. It is used to access attributes and methods of the object (instance) within the class.
1. For instance(object) methods (like display()), self is mandatory because the method needs to operate on the instance.
2. here in python, we don't need to declare attributes/variables in private part, we declare and assign variable/attributes directly in the constructor(__init__)
"""
class Person:
    #construtor to initialize attributes
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, age: {self.age}")

#class instance(object)
person1 = Person("Sana",20)
person1.display()

"""
Challenge 1: Class and Object
Create a class Car with attributes brand, model, and year.
Add a method car_info() to display the car details.
Create two objects of the class and call car_info() for both.
"""
class Car:
    def __init__(self, brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def car_info(self):
        print("Car Details:\n")
        print(f"Brand: {self.brand}\n")
        print(f"model: {self.model}\n")
        print(f"year: {self.year}\n")

toyota = Car("Toyota",1964,2020)
toyota.car_info()

mercedes= Car("Mercedes",2000,2024)
mercedes.car_info()

# 2. Inheritance
# Inheritance allows one class to derive (inherit) properties and methods from another.

# Base class (Parent)
class Animal:
    def speak(self):
        print("I make a sound")

# Derived class (Child)
class Dog(Animal):
    def speak(self):
        print("I bark")

# Create objects of both classes
animal = Animal()
dog = Dog()

animal.speak()  # Output: I make a sound
dog.speak()     # Output: I bark

"""
Challenge 2: Inheritance
Create a base class Shape with a method area().
Create a derived class Rectangle with attributes length and width, and override the area() method.
Create an object of Rectangle, set its attributes, and call the area() method.
"""

#base class
class Shape:
    def area(self):
        print("this is our shape area")

#derived class 
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length *self.width


rect1 = Rectangle(10,20)
print(rect1.area())

# 3. Encapsulation
# Encapsulation is about restricting direct access to some of an object's attributes and methods.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

# Create an account
account = BankAccount(1000)

# Deposit and withdraw
account.deposit(500)
account.withdraw(300)
print(account.get_balance())  # Output: 1200

"""
Challenge 3: Encapsulation
Create a class Student with private attributes name and grades.
Add methods to:
Set the student's name and grades.
Get the student's average grade.
Create an object and test all methods.
"""
class Student:
    def __init__(self,name,grades):
        self.__name = name   #private variable
        self.__grades = grades  #private variable

    def set_Name(self,name):
        self.__name = name
    def set_Grades(self,grades):
        self.__grades = grades
    def get_Grades(self):
        return self.__grades
    def get_Name(self):
        return self.__name

sana = Student("Sana",'A')
print(sana.get_Name())
print(sana.get_Grades())
sana.set_Grades('B+')
print(sana.get_Grades())