# 21 - Library Book Management System
import csv
import os

FILENAME = "books.csv"

def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["BookID", "Title", "Author", "Available"])
            writer.writerows([
                [1, "Python Programming", "Guido van Rossum", "Yes"],
                [2, "Data Structures",    "Mark Allen Weiss", "Yes"],
                [3, "Operating Systems",  "Silberschatz",      "Yes"],
            ])
        print("Library initialized with sample books.\n")

def load_books():
    with open(FILENAME, "r") as f:
        return list(csv.DictReader(f))

def save_books(books):
    with open(FILENAME, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["BookID","Title","Author","Available"])
        writer.writeheader()
        writer.writerows(books)

def add_book():
    books = load_books()
    new_id = max(int(b["BookID"]) for b in books) + 1 if books else 1
    title  = input("Enter book title: ")
    author = input("Enter author name: ")
    books.append({"BookID": new_id, "Title": title, "Author": author, "Available": "Yes"})
    save_books(books)
    print(f"Book '{title}' added with ID {new_id}.")

def search_book():
    keyword = input("Enter title or author to search: ").lower()
    books = load_books()
    results = [b for b in books if keyword in b["Title"].lower() or keyword in b["Author"].lower()]
    if results:
        for b in results:
            print(f"  ID:{b['BookID']} | {b['Title']} by {b['Author']} | Available: {b['Available']}")
    else:
        print("No matching books found.")

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    books = load_books()
    for b in books:
        if b["BookID"] == book_id:
            if b["Available"] == "Yes":
                b["Available"] = "No"
                save_books(books)
                print(f"Book '{b['Title']}' issued successfully.")
            else:
                print(f"Book '{b['Title']}' is already issued.")
            return
    print("Book not found.")

def return_book():
    book_id = input("Enter Book ID to return: ")
    books = load_books()
    for b in books:
        if b["BookID"] == book_id:
            b["Available"] = "Yes"
            save_books(books)
            print(f"Book '{b['Title']}' returned successfully.")
            return
    print("Book not found.")

def display_available():
    books = load_books()
    available = [b for b in books if b["Available"] == "Yes"]
    if available:
        print(f"{'ID':<6}{'Title':<30}{'Author':<25}")
        print("-" * 61)
        for b in available:
            print(f"{b['BookID']:<6}{b['Title']:<30}{b['Author']:<25}")
    else:
        print("No books currently available.")

initialize_file()

while True:
    print("\n=== Library Menu ===")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")
    choice = input("Enter choice: ")
    if choice == "1":   add_book()
    elif choice == "2": search_book()
    elif choice == "3": issue_book()
    elif choice == "4": return_book()
    elif choice == "5": display_available()
    elif choice == "6": break
    else: print("Invalid choice.")
