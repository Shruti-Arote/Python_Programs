#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shree Sai
#
# Created:     06-08-2024
# Copyright:   (c) Shree Sai 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------



#strings

name = "shruti Arote"

print(name.upper())
print(name)

print (name.find('A'))

print (name.replace("shruti","Snehal"))

print ("a" in name)


# Calculator
first = input("Enter first number:")
operator = input("Enter operato(+,-,*,%):")
second = input("Enter second number:")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)

elif operator == "-":
    print(first - second)

elif operator == "/":
    print(first / second)

elif operator == "*":
    print(first * second)

elif operator == "%":
    print(first % second)

else:
    print("Invalid Operation")



