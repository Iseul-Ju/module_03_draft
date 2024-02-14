import random
import os
from time import sleep

# Set of transaction options
transaction_options = {"D", "W", "Q"}

# Generate random bank balance
bank_balance = float(random.randint(-1000, 10000))

# Function to display current balance
def display_balance(balance):
    print("*" * 40)
    print("{:^40}".format("PIXELL RIVER FINANCIAL"))
    print("{:^40}".format("ATM Simulator"))
    print("{:^40}".format(f"Your current balance is: ${balance:,.2f}"))
    print("{:^40}".format("Deposit: D"))
    print("{:^40}".format("Withdraw: W"))
    print("{:^40}".format("Quit: Q"))
    print("*" * 40)
    print()

# Print initial ATM interface
display_balance(bank_balance)

# Main loop for multiple transactions
while True:
    # Prompt user for selection
    selection = input("Enter your selection: ").upper()

    # Validate selection
    if selection not in transaction_options:
        # Display invalid selection message
        print("*" * 40)
        print("{:^40}".format("INVALID SELECTION"))
        print("*" * 40)
        print()
    else:
        # Process valid selection
        if selection == "D" or selection == "W":
            amount = float(input("Enter amount of transaction: "))
            if selection == "D":
                bank_balance += amount
            elif selection == "W":
                if amount > bank_balance:
                    # Display insufficient funds message
                    print("*" * 40)
                    print("{:^40}".format("INSUFFICIENT FUNDS"))
                    print("*" * 40)
                    print()
                else:
                    bank_balance -= amount
            display_balance(bank_balance)
        elif selection == "Q":
            break

# Pause and clear the screen after 3 seconds
sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')