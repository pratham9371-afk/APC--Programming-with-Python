# 17 - Student Records - CSV file operations
import csv
import os

FILENAME = "students_records.csv"

def create_file():
    records = [
        ["RollNo", "Name",  "Marks"],
        [101,      "Amit",   85],
        [102,      "Priya",  92],
        [103,      "Rahul",  78],
        [104,      "Sneha",  88],
        [105,      "Karan",  70],
    ]
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(records)
    print(f"'{FILENAME}' created.\n")

def load_records():
    with open(FILENAME, "r") as f:
        reader = csv.DictReader(f)
        return [{"RollNo": int(r["RollNo"]), "Name": r["Name"], "Marks": int(r["Marks"])} for r in reader]

def display_all(records):
    print(f"{'RollNo':<10}{'Name':<15}{'Marks':<10}")
    print("-" * 35)
    for r in records:
        print(f"{r['RollNo']:<10}{r['Name']:<15}{r['Marks']:<10}")

def highest_marks(records):
    top = max(records, key=lambda r: r["Marks"])
    print(f"\nStudent with highest marks: {top['Name']} ({top['Marks']})")

def average_marks(records):
    avg = sum(r["Marks"] for r in records) / len(records)
    print(f"Average marks: {avg:.2f}")

def above_80(records):
    print("\nStudents who scored more than 80:")
    for r in records:
        if r["Marks"] > 80:
            print(f"  {r['Name']} - {r['Marks']}")

if not os.path.exists(FILENAME):
    create_file()

records = load_records()
print("=== All Records ===")
display_all(records)
highest_marks(records)
average_marks(records)
above_80(records)
