from pprint import pprint

# Define an empty dictionary to store the contents of the input file
data = {}

# Open the input file named account_balances.txt
with open("account_balances.txt", "r") as file:
    for line in file:
        account_number, account_balance = line.strip().split("|")
        data[account_number] = float(account_balance)

# Display the contents of the dictionary
pprint(data)

