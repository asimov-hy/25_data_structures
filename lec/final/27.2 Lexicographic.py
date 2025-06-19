def lexicographic_bucket_sort(strings):
    """
    Bucket Sort for strings based on their first character (assuming lowercase a–z).
    Sorts lexicographically by first letter.
    """
    # 1. Create 26 buckets for each letter a–z
    buckets = [[] for _ in range(26)]

    # 2. Place each string into the corresponding bucket based on first character
    for s in strings:
        if not s: continue  # skip empty strings
        index = ord(s[0]) - ord('a')  # 'a' → 0, 'b' → 1, ..., 'z' → 25
        buckets[index].append(s)

    # 3. Flatten the buckets in order
    sorted_strings = []
    for bucket in buckets:
        sorted_strings.extend(bucket)  # preserve order within each bucket

    return sorted_strings


words = ["banana", "apple", "carrot", "avocado", "blueberry", "cherry"]
sorted_words = lexicographic_bucket_sort(words)
print("Lexicographically sorted:", sorted_words)
