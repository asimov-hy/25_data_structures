"""
Merge Sort Implementation
--------------------------
A divide-and-conquer sorting algorithm with O(n log n) time complexity.

Functions:
----------
- `merge_sort(arr)`:
  1. Recursively divides the input list into halves.
  2. Sorts each half.
  3. Merges the sorted halves into a single sorted list.

- `merge(left, right)`:
  - Merges two sorted lists into one sorted list.
  - Compares elements from both sides and merges in ascending order.
  - Appends any remaining elements after one side is exhausted.

Properties:
-----------
- Stable sort (preserves order of equal elements).
- Not in-place (uses extra memory for merging).
- Guarantees consistent performance (O(n log n) worst case).
"""


def merge_sort(arr):
    # 1. Base case: list of size 0 or 1 is already sorted
    if len(arr) <= 1:
        return arr

    # 2. Divide step: split array into two halves
    mid = len(arr) // 2
    left = arr[:mid]     # first half
    right = arr[mid:]    # second half

    # 3. Conquer step: recursively sort each half
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # 4. Combine step: merge two sorted halves
    return merge(sorted_left, sorted_right)

def merge(left, right):
    # 1. Create a new empty result list
    result = []
    i = j = 0

    # 2. While both lists have elements, compare and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])  # take from left
            i += 1
        else:
            result.append(right[j])  # take from right
            j += 1

    # 3. Append remaining elements (if any)
    result.extend(left[i:])   # leftover in left
    result.extend(right[j:])  # leftover in right

    return result
