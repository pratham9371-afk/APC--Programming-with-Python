# 22 - Merge two text files into a third file
def merge_files(file1, file2, output_file):
    try:
        with open(file1, "r") as f1:
            content1 = f1.read()
        with open(file2, "r") as f2:
            content2 = f2.read()
        with open(output_file, "w") as fout:
            fout.write(f"=== Contents of '{file1}' ===\n")
            fout.write(content1)
            fout.write(f"\n\n=== Contents of '{file2}' ===\n")
            fout.write(content2)
        print(f"Files merged successfully into '{output_file}'.")
    except FileNotFoundError as e:
        print(f"Error: {e}")

f1 = input("Enter first filename: ")
f2 = input("Enter second filename: ")
out = input("Enter output filename: ")
merge_files(f1, f2, out)
