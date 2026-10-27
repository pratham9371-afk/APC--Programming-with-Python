# 20 - Bank Transactions - Deposits, Withdrawals, Balance, Largest Transaction
import csv
import os

FILENAME = "transactions.csv"

def create_file():
    records = [
        ["Type",       "Amount"],
        ["Deposit",     5000],
        ["Withdrawal",  1500],
        ["Deposit",     3000],
        ["Withdrawal",   800],
        ["Deposit",    10000],
        ["Withdrawal",  2500],
        ["Deposit",     1200],
    ]
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(records)
    print(f"'{FILENAME}' created.\n")

def analyze_transactions():
    total_deposit = total_withdrawal = 0
    largest = 0
    largest_type = ""
    with open(FILENAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            amount = int(row["Amount"])
            if row["Type"] == "Deposit":
                total_deposit += amount
            else:
                total_withdrawal += amount
            if amount > largest:
                largest = amount
                largest_type = row["Type"]

    balance = total_deposit - total_withdrawal
    print(f"Total Deposits    : {total_deposit}")
    print(f"Total Withdrawals : {total_withdrawal}")
    print(f"Final Balance     : {balance}")
    print(f"Largest Transaction: {largest_type} of {largest}")

if not os.path.exists(FILENAME):
    create_file()

analyze_transactions()
