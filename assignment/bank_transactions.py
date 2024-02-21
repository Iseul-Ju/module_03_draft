"""
Description: Flow of Control: Applying Logic and Loops to a Python Program
Author: Nathan Ascano
Date: February 14, 2024
"""

# import statements
import random
import os
from time import sleep

# transaction options of deposit, withdraw and quit as a set
options = {'D', 'W', 'Q'}

# user's balance as a float.
balance = float(random.randint(-1000, 10000))

# main program loop
while True:
    # displaying ATM interface
    print("***************************************")
    print("PIXELL RIVER FINANCIAL".center(40))
    print("ATM Simulator".center(40))
    # doing the formal formatting to show the balance
    print(f"Your current balance is: ${balance:,.2f}".center(40))
    print("")
    print("Deposit: D".center(40))
    print("Withdraw: W".center(40))
    print("Quit: Q".center(40))
    print("***************************************")
    
    # prompt user for selection
    selection = input("Enter your selection: ").upper()
    
    # validate selection
    if selection not in options:
        print("***************************************")
        print("INVALID SELECTION".center(40))
        print("***************************************")
    else:
        # process valid selection
        if selection == "D":
            amount = float(input("Enter amount of deposit: "))
            balance += amount
        elif selection == "W":
            amount = float(input("Enter amount of withdrawal: "))
            if amount > balance:
                print("***************************************")
                print("INSUFFICIENT FUNDS".center(40))
                print("***************************************")
            else:
                balance -= amount
        elif selection == "Q":
            break  # break command to end the loop
        
    # makes the program pause for 3 seconds then clears the screen afterwards
    sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

# makes it pause 3 seconds before delivering the end statement message
sleep(1)
# end statement message
print("Thank you for using PIXELL RIVER FINANCIAL ATM Simulator!")