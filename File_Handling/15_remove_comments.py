# 15 - Remove single-line comments from a Python source file
def remove_comments(source_file, output_file):
    try:
        with open(source_file, "r") as f:
            lines = f.readlines()
        cleaned = []
        for line in lines:
            stripped = line.lstrip()
            # Remove lines that are purely comments
            if stripped.startswith("#"):
                continue
            # Remove inline comments
            if "#" in line:
                line = line[:line.index("#")] + "\n"
            cleaned.append(line)
        with open(output_file, "w") as f:
            f.writelines(cleaned)
        print(f"Comments removed. Output saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: '{source_file}' not found.")

src = input("Enter source Python filename: ")
out = input("Enter output filename: ")
remove_comments(src, out)
