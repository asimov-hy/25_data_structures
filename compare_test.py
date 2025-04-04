import sys

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    max_len = max(len(lines1), len(lines2))
    match = True

    for i in range(max_len):
        line_num = i + 1

        # Get lines or fallback to empty string if one file is shorter
        l1 = lines1[i].rstrip() if i < len(lines1) else "<EOF>"
        l2 = lines2[i].rstrip() if i < len(lines2) else "<EOF>"

        if l1 != l2:
            print(f"❌ Difference at line {line_num}:")
            print(f"File 1: {l1}")
            print(f"File 2: {l2}")
            match = False
            break

    if match:
        print("✅ Files match exactly!")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_outputs.py <file1.out> <file2.out>")
    else:
        compare_files(sys.argv[1], sys.argv[2])
