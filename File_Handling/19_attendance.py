# 19 - Student Attendance - Calculate percentage and find low-attendance students
import csv
import os

FILENAME = "attendance.csv"

def create_file():
    records = [
        ["RollNo", "Name",    "TotalClasses", "Attended"],
        [101,      "Amit",     60,              55],
        [102,      "Priya",    60,              40],
        [103,      "Rahul",    60,              58],
        [104,      "Sneha",    60,              42],
        [105,      "Karan",    60,              50],
    ]
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(records)
    print(f"'{FILENAME}' created.\n")

def load_attendance():
    with open(FILENAME, "r") as f:
        reader = csv.DictReader(f)
        return [{"RollNo": int(r["RollNo"]), "Name": r["Name"],
                 "TotalClasses": int(r["TotalClasses"]),
                 "Attended": int(r["Attended"])} for r in reader]

def calculate_and_display(records):
    print(f"{'RollNo':<10}{'Name':<12}{'Attended':<10}{'Total':<10}{'Percentage':<12}{'Status'}")
    print("-" * 60)
    below_75 = []
    for r in records:
        pct = (r["Attended"] / r["TotalClasses"]) * 100
        status = "OK" if pct >= 75 else "LOW"
        print(f"{r['RollNo']:<10}{r['Name']:<12}{r['Attended']:<10}{r['TotalClasses']:<10}{pct:<12.2f}{status}")
        if pct < 75:
            below_75.append((r["Name"], pct))
    if below_75:
        print("\nStudents with attendance below 75%:")
        for name, pct in below_75:
            print(f"  {name}: {pct:.2f}%")

if not os.path.exists(FILENAME):
    create_file()

records = load_attendance()
calculate_and_display(records)
