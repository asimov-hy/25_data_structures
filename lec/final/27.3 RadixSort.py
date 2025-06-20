"""
Radix Sort for Fixed-Length Strings
-----------------------------------

Sorts a list of lowercase strings (same length) in lexicographic order.

Function:
- `radix_sort(strings)`:
  1. Iterate from the last character to the first (right to left).
  2. For each character position:
     - Distribute strings into 26 buckets based on the current character.
     - Concatenate buckets to update the list.

Uses stable bucket sort at each character position to preserve previous order.
"""


def radix_sort(strings):
    """
    Radix Sort for fixed-length lowercase strings (e.g., 'cat', 'dog').
    Sorts strings in lexicographic order using character-wise bucket sort.
    Assumes all strings are the same length.
    """
    if not strings:
        return []

    # 1. Get fixed string length
    w = len(strings[0])

    # 2. Perform bucket sort from last char to first (right to left)
    for i in reversed(range(w)):
        # 2-1. Create 26 buckets for 'a' to 'z'
        buckets = [[] for _ in range(26)]

        # 2-2. Distribute strings by character at position i
        for s in strings:
            index = ord(s[i]) - ord('a')  # convert char to bucket index
            buckets[index].append(s)

        # 2-3. Recombine strings in order (stable)
        strings = [s for bucket in buckets for s in bucket]

    return strings

words = ['dog', 'cat', 'bat', 'cow', 'ant', 'ape']
sorted_words = radix_sort(words)
print("Sorted:", sorted_words)

# Output: Sorted: ['ant', 'ape', 'bat', 'cat', 'cow', 'dog']