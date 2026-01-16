# Defintion

# The built in function input() is used to receive nput from the keyboard.
# input() function returns entered value as string so to reveive an integer/float value from user we need to convert with respective convert function.

# Code

name = input("Enter your Name : ")  # Receives String value from the user
age = int(input("Enter your Age : "))  # Receives an Integer value from the user "int()"
weight = float(input("Enter your weight : ")) # Receives an Float value from the user '"float()"

print(f"Hello My Name is {name} ! ")
print(f"My Age is {age} years old ")
print(f"My weight is {weight} kgs ")

