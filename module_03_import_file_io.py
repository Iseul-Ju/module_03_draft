"""
Description: Introduction to Import Statements and File I/O
Author: Student Name
Date: September 2023
Usage: To execute, press the play button in the VSC IDE.
"""
# IMPORT STATEMENTS
import math as m
from math import sqrt
import random
from pprint import pprint

# Variables used in this demonstration
radius = 12.5
square = 144
fruits = ["apple", "banana", "cherry"]

# USING IMPORTED MODULES
area = m.pi * radius ** 2
print(area)

root = sqrt(square)
print(root)

# RANDOM
print(random.random())  

print(random.randint(1, 6))  

print(random.choice(fruits))  

random.shuffle(fruits)
print(fruits)  # Output: list is rearranged


# FILE I/O
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Writing to a file
file = open("output.txt", "w")
file.write("Hello world!")
file.close()


# WITH CLAUSE
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


# READ INTO DICTIONARY
data = {}
with open("dict_example.txt", "r") as input_file:
    for line in input_file:
        # 1st line = John*100
        key, value = line.strip().split('*')
        data[key] = int(value)

print(data)
pprint(data)
