#import statement.
import random

#transaction options of deposit, withdraw and quit as a set.
options = {'D', 'W', 'Q'}

#user's balance as a float.
balance = float(random.randint(-1000, 10000))

# Function to display current balance
def display_balance(balance):
    print("***************************************")
    print("PIXELL RIVER FINANCIAL".center(40))
    print("ATM Simulator".center(40))
    print(f"Your current balance is: ${balance:,.2f}".center(40))
    print("")
    print("Deposit: D".center(40))
    print("Withdraw: W".center(40))
    print("Quit: Q".center(40))
    print("***************************************")

# Main program loop
while True:
    # Display ATM interface
    display_balance(balance)
    
    # Prompt user for selection
    selection = input("Enter your selection: ").upper()
    
    # Validate selection
    if selection not in options:
        print("***************************************")
        print("INVALID SELECTION".center(40))
        print("***************************************")
    else:
        # Process valid selection
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
            break  # Quit action, exit the loop

print("Thank you for using PIXELL RIVER FINANCIAL ATM Simulator!")
