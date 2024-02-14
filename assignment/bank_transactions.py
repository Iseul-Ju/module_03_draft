
"""
Description: Flow of Control: Applying Logic and Loops to a Python Program
Author: Nathan Ascano
Date: February 14, 2024
"""
import random

#transaction options of deposit, withdraw and quit as a set.
options = {"D", "W", "Q"}

#user's balance as a float.
balance = float(random.randint(-1000, 10000))

#defining the print statements to display the interface from the instructions and centering them with a width of 40 characters.
print("***************************************")
print("PIXELL RIVER FINANCIAL".center(40))
print("ATM Simulator".center(40))
#doing the formal formatting to show the balance.
print(f"Your current balance is: ${balance:,.2f}".center(40))
print("")
print("Deposit: D".center(40))
print("Withdraw: W".center(40))
print("Quit: Q".center(40))
print("***************************************")

