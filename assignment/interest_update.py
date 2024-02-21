"""
Description: Flow of Control: Applying Logic and Loops to a Python Program
Author: Nathan Ascano
Date: February 14, 2024
"""

# import statements
import csv
from pprint import pprint

# 2. Display Current Balances

# defining empty dictionaty to store contents of input file
data = {}

# opening input file account_balances.txt
with open("account_balances.txt", "r") as file:
    for line in file:
        account_number, balance = line.strip().split("|")
        data[account_number] = float(balance)

# displaying contents of dictionary using pprint
print("Current Balances:")
pprint(data)

# 3. Incorporate Transactions

# iterating through the dictionary of bank records
for account_number, balance in data.items():
    # calculating interest
    if balance > 0:
        if balance < 1000:
            rate = 0.01
        elif balance < 5000 and balance >= 1000:
            rate = 0.025
        else:
            rate = 0.05
    else:
        rate = 0.1
    # forumula for applying interest
    updated_balance = balance + ((balance * rate) / 12)
    # updating the balance
    data[account_number] = float(updated_balance)

# displaying the balance
print()
print("Updated Balances with Interest:")
pprint(data)

# 4. Write the Updated Data

# defining the filename
filename = "updated_balances_NA.csv"

# opening csv file using write mode
with open(filename, "w", newline="") as csvfile:
    # defining the headings as account and balance
    fieldnames = ["Account", "Balance"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # writing the headings
    writer.writeheader()
    
    # writing updated records
    for account_number, balance in data.items():
        writer.writerow({"Account": account_number, "Balance": balance})
print()
print(f"Data has been successfully written to {filename}")

# 5. Display the Updated Data

# opening csv file in read mode
with open(filename, "r") as csvfile:

    # reading the file using DictReader
    reader = csv.DictReader(csvfile)

    # printing the contents to the console
    print()
    print("Updated Data:")
    for row in reader:
        print(row)