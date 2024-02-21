"""
Description: Flow of Control: Applying Logic and Loops to a Python Program
Author: Nathan Ascano
Date: February 14, 2024
"""

import csv
from pprint import pprint

# 2. Display Current Balances

# Define an empty dictionary to store the contents of the input file
data = {}

# Open the input file named account_balances.txt
with open("account_balances.txt", "r") as file:
    for line in file:
        account_number, balance = line.strip().split("|")
        data[account_number] = float(balance)

# Display the contents of the dictionary
print("Current Balances:")
pprint(data)

# 3. Incorporate Transactions

# Iterate through the dictionary of bank records
for account_number, balance in data.items():
    # Determine interest rate based on balance
    if balance > 0:
        if balance < 1000:
            rate = 0.01
        elif balance < 5000 and balance >= 1000:
            rate = 0.025
        else:
            rate = 0.05
    else:
        rate = 0.1
    # Apply monthly interest
    updated_balance = balance + ((balance * rate) / 12)
    # Update the balance in the dictionary
    data[account_number] = float(updated_balance)

# Display the updated balances
print()
print("Updated Balances with Interest:")
pprint(data)

# 4. Write the Updated Data

# Define the filename
filename = "updated_balances_NA.csv"

# Open the csv file in write mode
with open(filename, "w", newline="") as csvfile:
    # Define headings
    fieldnames = ["Account", "Balance"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write headings
    writer.writeheader()
    
    # Write updated records
    for account_number, balance in data.items():
        writer.writerow({"Account": account_number, "Balance": balance})
print()
print(f"Data has been successfully written to {filename}")

# 5. Display the Updated Data

# Open the csv file in read mode
with open(filename) as csvfile:
    # Read the file using DictReader
    reader = csv.DictReader(csvfile)
    
    # Print the contents to the console
    print()
    print("Updated Data:")
    for row in reader:
        print(row)