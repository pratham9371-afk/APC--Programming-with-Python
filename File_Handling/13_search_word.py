# 13 - Search for a word in a text file and display occurrences and line numbers
def search_word(filename, search_term):
    try:
        occurrences = 0
        line_numbers = []
        with open(filename, "r") as f:
            for line_no, line in enumerate(f, start=1):
                count = line.lower().count(search_term.lower())
                if count > 0:
                    occurrences += count
                    line_numbers.append(line_no)
        if occurrences:
            print(f"Word '{search_term}' found {occurrences} time(s).")
            print(f"Appears on line(s): {line_numbers}")
        else:
            print(f"Word '{search_term}' not found in '{filename}'.")
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

filename = "student.txt"
word = input("Enter a word to search: ")
search_word(filename, word)
