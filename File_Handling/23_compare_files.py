# 23 - Compare two text files and display differences
def compare_files(file1, file2):
    try:
        with open(file1, "r") as f1:
            lines1 = f1.readlines()
        with open(file2, "r") as f2:
            lines2 = f2.readlines()

        if lines1 == lines2:
            print(f"'{file1}' and '{file2}' are IDENTICAL.")
        else:
            print(f"'{file1}' and '{file2}' are DIFFERENT.")
            max_len = max(len(lines1), len(lines2))
            for i in range(max_len):
                l1 = lines1[i] if i < len(lines1) else "<missing>"
                l2 = lines2[i] if i < len(lines2) else "<missing>"
                if l1 != l2:
                    print(f"\nFirst difference at line {i + 1}:")
                    print(f"  File1: {l1.rstrip()}")
                    print(f"  File2: {l2.rstrip()}")
                    break
    except FileNotFoundError as e:
        print(f"Error: {e}")

f1 = input("Enter first filename: ")
f2 = input("Enter second filename: ")
compare_files(f1, f2)
