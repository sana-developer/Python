"""
List
A list is ordered and mutable(can be changed)
"""
# Create a list
fruits = ["apple", "banana", "cherry"]

# Access elements
print(fruits[0])  # Output: apple

# Add and remove items
fruits.append("orange")  # Add at the end
fruits.remove("banana")  # Remove an item
print(fruits)

# Loop through a list
for fruit in fruits:
    print(f"I like {fruit}")



#Tuple: a tuple is immutable(cannot be changed)
# Create a tuple
dimensions = (1920, 1080)

# Access elements
print(dimensions[0])  # Output: 1920

# Tuples cannot be modified!
# dimensions[0] = 1280  # This will raise an error


#dictionary: stores key/value pairs

#create a dictionary
student = {
    "name": "Sana",
    "age": 21,
    "skills": ["c++","python"]
}

#accessing values
print(student["name"])  # Output: Sana
print(student["skills"][0])  # Output: c++
print(student.get("age"))  # Output: 21 (using get method)

#add/update key/value pair
student["degree"] = "Bachlors in software engineering"
student["age"] = 22

print(student)

#loop through key and values
for key,value in student.items():
    print(f"{key}:{value}")


#set: is unordered collection of unique items.
numbers = {1,2,3,3,4}

print(numbers) #Output: {1, 2, 3, 4} (duplicates are removed)

#add and remove elements
numbers.add(8)
numbers.remove(3)

print(numbers)



#Challanges
"""
Challenge 1: List Operations
Create a list of your favorite colors.
Add two new colors to the list.
Remove one color from the list.
Print the final list.
"""

colours=["red","green","purple"]
colours.append("black")
colours.append("white")
colours.remove("green")
for colour in colours:
    print(f"colour: {colour}")


# Challenge 2: Tuple and Dictionary
# Create a tuple for your room dimensions (length, width).
dimensions = (45,90) #in inches
# Create a dictionary with your profile:
# Name
# Age
# Favorite programming languages (as a list).
profile={
    "Name": "Sana",
    "Age": 20,
    "fav prog languages": ["C++","react"]
}
# Print the dictionary and access each value individually.
print(profile)
for key,value in profile.items():
    print(f"{key}: {value}")


# Challenge 3: Set Operations
# Create a set of even numbers from 1 to 10.
even_numbers={2,4,6,8,10}
# Add the number 12 to the set.
even_numbers.add(12)
# Remove the number 6 from the set.
even_numbers.remove(6)
# Print the final set.
for num in even_numbers:
    print(f"Number:{num}")