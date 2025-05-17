def compare_files(file1, file2): 
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    max_len = max(len(lines1), len(lines2))
    match = True

    for i in range(max_len):
        line_num = i + 1

        l1 = lines1[i].rstrip() if i < len(lines1) else "<EOF>"
        l2 = lines2[i].rstrip() if i < len(lines2) else "<EOF>"

        if l1 != l2:
            print(f"❌ Difference at line {line_num}:")
            print(f"{file1}: {l1}")
            print(f"{file2}: {l2}")
            match = False
            break

    if match:
        print("✅ Files match exactly!")


if __name__ == "__main__":
    file1 = "mytestout.out"
    file2 = "test.0.4.out"
    compare_files(file1, file2)
