# 16 - Read a text file and write its content in uppercase to another file
def convert_to_uppercase(source_file, output_file):
    try:
        with open(source_file, "r") as f:
            content = f.read()
        with open(output_file, "w") as f:
            f.write(content.upper())
        print(f"Uppercase version saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: '{source_file}' not found.")

src = "student.txt"
out = "student_upper.txt"
convert_to_uppercase(src, out)
with open(out, "r") as f:
    print(f.read())
