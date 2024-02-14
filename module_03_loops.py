"""
Description: Introduction to Loops
Author: Nathan
Date: February 2024
Usage: To execute, press the play button in the VSC IDE.
"""

# Variables used in this demonstration:
fruits = ["apple", "orange", "banana", "cherry"]
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# FOR LOOP
for i in range(100):
    print(i)

for number in range(2, 8):
    print(number)

for i in range(1, 10, 2):
    print(i)

for i in range(-10, 0):
    print(i)


# INPUT FUNCTION
name = input('What is your name?')
salary = float(input('What is your current salary?'))

print(f"Name: {name} \nSalary: ${salary:,.2f}")  #(do exepction handling. 51 mins in demo to make sure user types in the proper answer)


# WHILE LOOP     #CTRL C to interrupt stuff

favorite_number = 0
#while favorite_number != 100:
#    favorite_number = int(input("Enter your favorite number, 100 & up to quit: "))

"""
favorite_number = 0
while favorite_number < 100:
    favorite_number = int(input("Enter your favorite number, 100 & up to quit: "))
else:
    print("Your favorite number is too big!")
"""
"""
# BREAK
while favorite_number < 100:
    favorite_number = int(input("Enter your favorite number (but not 7), 100 to quit: "))
    if favorite_number == 7:
        print("You broke this game!")
        break
else:
    print("Your favorite number is too big!")
"""

# CONTINUE
# LOOP CONTROL STATEMENTS
# Use a for loop to iterate over the range of integers from 1 to 9 (exclusive).
for number in range(1, 10):
    # Use continue statement to skip over multiples of 3.
    if number % 3 == 0:
        #print("1st", number)
        continue
    # Print all other integers
    print(number)


#BREAK
# Use a for loop to iterate over the range of integers 
for number in range(1, 10):
    # Use the break statement to exit the loop if the integer is greater than 5
    if number > 5:
        break
    # Print all other integers.
    print(number)


# INFINITE LOOP
# <ctrl> + c (in the terminal window) to stop an infinite loop in VS Code.
"""
number = 10
while number > 0:
    number += 1 # equivalent to number = number + 1
    print(number)
"""

# to prevent the infinite loop
"""
number = 10
while number > 0:
    if number > 100:
        break
    number += 1
    print(number)
"""

# NESTED LOOP
# matrix variable defined at top of editor.

# for every iteration of outer loop, inner loop will execute in its entirety
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in matrix:
    for element in row:
        # end = ' ' overrides the line feed with a space
        print(element, end= ' ')
    # Use the empty print() function for line feed after row 
    print()
