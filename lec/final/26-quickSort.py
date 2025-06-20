"""
Quick Sort and In-Place Quick Sort
----------------------------------

Functions:
- `quick_sort(arr)`:
  1. Base case: if size ≤ 1, return as-is.
  2. Choose a random pivot.
  3. Partition into:
     - L: elements < pivot
     - E: elements = pivot
     - G: elements > pivot
  4. Recursively sort L and G.
  5. Concatenate sorted L, E, and G.

- `in_place_quick_sort(arr, low, high)`:
  1. Base case: stop when subarray has ≤ 1 element.
  2. Choose a random pivot and move it to the end.
  3. Partition the array (Lomuto partition scheme).
  4. Recursively sort the left and right subarrays in place.
"""


def quick_sort(arr):
    # 1. Base case: array of size 0 or 1 is already sorted
    if len(arr) <= 1:
        return arr

    # 2. Divide: pick a pivot element at random
    from random import choice
    pivot = choice(arr)

    # 3. Partition: split array into 3 parts
    #    L: elements less than pivot
    #    E: elements equal to pivot
    #    G: elements greater than pivot
    L, E, G = [], [], []
    for x in arr:
        if x < pivot:
            L.append(x)
        elif x == pivot:
            E.append(x)
        else:
            G.append(x)

    # 4. Conquer: recursively sort L and G
    sorted_L = quick_sort(L)
    sorted_G = quick_sort(G)

    # 5. Combine: concatenate sorted parts
    return sorted_L + E + sorted_G

arr = [7, 4, 9, 6, 2]
sorted_arr = quick_sort(arr)
print("Sorted:", sorted_arr)

# --------------------------- In-Place Quick Sort ---------------------------
# In-place quick sort modifies the array directly without using additional space for L, E, G.

def in_place_quick_sort(arr, low=0, high=None):
    # 1. Initial setup
    if high is None:
        high = len(arr) - 1

    # 2. Base case
    if low >= high:
        return

    # 3. Choose pivot randomly and partition
    from random import randint
    pivot_index = randint(low, high)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move pivot to end

    # 4. Partitioning process (Lomuto-style)
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # 5. Place pivot in correct position
    arr[i], arr[high] = arr[high], arr[i]

    # 6. Recursive sort on left and right
    in_place_quick_sort(arr, low, i - 1)
    in_place_quick_sort(arr, i + 1, high)


arr = [7, 4, 9, 6, 2]
in_place_quick_sort(arr)
print("In-place sorted:", arr)
