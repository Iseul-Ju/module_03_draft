import random

# Set of transaction options
transaction_options = {"D", "W", "Q"}
print(type(transaction_options)) 

# Generate random bank balance
bank_balance = float(random.randint(-1000, 10000))

# Format balance as currency string
formatted_balance = "${:,.2f}".format(bank_balance)

# Print ATM interface
print("*" * 40)
print("{:^40}".format("PIXELL RIVER FINANCIAL"))
print("{:^40}".format("ATM Simulator"))
print("{:^40}".format(f"Your current balance is: {formatted_balance}"))
print()
print("{:^40}".format("Deposit: D"))
print("{:^40}".format("Withdraw: W"))
print("{:^40}".format("Quit: Q"))
print("*" * 40)