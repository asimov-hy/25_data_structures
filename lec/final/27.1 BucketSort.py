"""
Bucket Sort for Integer Keys
----------------------------

Sorts a list of (key, value) pairs where keys are in the range [0, N−1].

Function:
- `bucket_sort(S, N)`:
  1. Create N empty buckets.
  2. Distribute each (key, value) pair into the bucket indexed by its key.
  3. Concatenate all buckets back into the original list `S`.

Maintains stability by preserving the original order within each bucket.
"""


# multiple buckets, sorts each bucket individually (often with another algorithm), and then concatenates all buckets to produce the sorted output.
# 12, 45, 24, 68, -> sort based on first digit, then second digit....

def bucket_sort(S, N):
    """
    Bucket Sort algorithm for integer keys in range [0, N−1]
    S: list of (key, value) pairs
    N: size of key range
    """
    # 1. Create N empty buckets
    B = [[] for _ in range(N)]

    # 2. Phase 1: Distribute entries into buckets
    for entry in S:
        key, value = entry
        B[key].append(entry)  # Place in bucket indexed by key

    # 3. Phase 2: Concatenate all buckets back to S
    S.clear()  # Empty the original list
    for i in range(N):
        for entry in B[i]:
            S.append(entry)  # Maintain stable order

    return S

S = [(7, 'd'), (1, 'c'), (3, 'a'), (7, 'g'), (3, 'b'), (7, 'e')]
N = 10  # Key range is 0 to 9

sorted_S = bucket_sort(S, N)
print("Sorted:", sorted_S)