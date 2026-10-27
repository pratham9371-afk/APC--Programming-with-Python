# 18 - Employee Records - File operations with functions
import csv
import os

FILENAME = "employees.csv"

def create_file():
    records = [
        ["EmpID", "Name",    "Department",  "Salary"],
        [1,       "Alice",   "IT",           75000],
        [2,       "Bob",     "HR",           55000],
        [3,       "Charlie", "Finance",      90000],
        [4,       "Diana",   "IT",           82000],
        [5,       "Edward",  "Marketing",    61000],
    ]
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(records)
    print(f"'{FILENAME}' created.\n")

def load_employees():
    with open(FILENAME, "r") as f:
        reader = csv.DictReader(f)
        return [{"EmpID": int(r["EmpID"]), "Name": r["Name"],
                 "Department": r["Department"], "Salary": int(r["Salary"])} for r in reader]

def display_all(employees):
    print(f"{'EmpID':<8}{'Name':<12}{'Department':<15}{'Salary':<10}")
    print("-" * 45)
    for e in employees:
        print(f"{e['EmpID']:<8}{e['Name']:<12}{e['Department']:<15}{e['Salary']:<10}")

def highest_paid(employees):
    top = max(employees, key=lambda e: e["Salary"])
    print(f"\nHighest-paid employee: {top['Name']} (Dept: {top['Department']}, Salary: {top['Salary']})")

def average_salary(employees):
    avg = sum(e["Salary"] for e in employees) / len(employees)
    print(f"Average salary: {avg:.2f}")

def above_salary(employees, threshold):
    print(f"\nEmployees earning above {threshold}:")
    for e in employees:
        if e["Salary"] > threshold:
            print(f"  {e['Name']} - {e['Salary']} ({e['Department']})")

if not os.path.exists(FILENAME):
    create_file()

employees = load_employees()
print("=== All Employees ===")
display_all(employees)
highest_paid(employees)
average_salary(employees)
threshold = int(input("\nEnter salary threshold: "))
above_salary(employees, threshold)
