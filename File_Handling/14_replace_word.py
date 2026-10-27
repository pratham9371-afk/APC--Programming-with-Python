# 14 - Replace a word in a text file and save to a new file
def replace_word(source_file, old_word, new_word, dest_file=None):
    try:
        with open(source_file, "r") as f:
            content = f.read()
        modified = content.replace(old_word, new_word)
        output_file = dest_file if dest_file else source_file
        with open(output_file, "w") as f:
            f.write(modified)
        count = content.count(old_word)
        print(f"Replaced '{old_word}' with '{new_word}' ({count} occurrence(s)).")
        print(f"Saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: '{source_file}' not found.")

source  = "student.txt"
old     = input("Enter the word to replace: ")
new     = input("Enter the new word: ")
output  = input("Enter output filename (press Enter to overwrite source): ").strip()
replace_word(source, old, new, output if output else None)
