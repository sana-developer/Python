print("first program in python")

#variables
name="Sana"
age=21
print(f"My name is {name} and I am {age} years old.")

#conditionals
age=22
if age>=18:
    print("You're an adult.")
else:
    print("You're young.")


#loops
#for loop
number=[1,2,3,4,5]
for num in number:
    print(f"number: {num}")

#while loop
count=4
while count>0:
    print("we are in while loop")
    count -= 1

#functions
def newfunc(name):
    return f"hii, {name}!"


#calling function
print(newfunc("Sana"))
print(newfunc(10))