"""
Dynamic Programming Examples
----------------------------

1. Matrix Chain Multiplication (matrix_chain):
   - Input: list d where matrix A[i] has dimensions d[i] × d[i+1]
   - Goal: minimize total scalar multiplications for multiplying A0 × A1 × ... × An−1
   - Returns: table N[i][j] where N[i][j] is the minimum cost to compute A[i..j]

2. Longest Common Subsequence (LCS):
   - Input: strings X and Y
   - Goal: compute length of the longest common subsequence
   - Returns: table L[i][j] with LCS length between X[0..i−1] and Y[0..j−1]

Key Idea:
- Solve problems by combining optimal solutions to overlapping subproblems.
- Use a 2D DP table to avoid recomputation and build up the solution efficiently.
"""


def matrix_chain(d):
    """
    Given dimensions d[0..n] where matrix A[i] has dimension d[i] x d[i+1],
    compute the minimum number of scalar multiplications needed to compute
    the product A0 × A1 × ... × An−1.

    Returns a 2D table N[i][j] with minimum cost of computing A[i..j].
    """
    n = len(d) - 1  # Number of matrices = len(d) - 1

    # Step 1: Initialize n × n cost matrix N with zeros
    N = [[0] * n for i in range(n)]

    # Step 2: Loop over increasing chain lengths b = 1 to n−1
    for b in range(1, n):
        # Step 3: For each subchain A[i..j] of length b+1
        for i in range(n - b):
            j = i + b  # end index of the subchain
            # Step 4: Find minimum cost among all split points k
            N[i][j] = min(
                N[i][k] + N[k + 1][j] + d[i] * d[k + 1] * d[j + 1]
                for k in range(i, j)
            )

    return N



def print_optimal_parens(s, i, j):
    """
    Recursively prints the optimal parenthesization for Ai..Aj.
    """
    if i == j:
        print(f"A{i}", end='')
    else:
        print("(", end='')
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end='')

# -------------------------------------- Longest Common Subsequence (LCS)--------------------------------------

def LCS(X, Y):
    """
    Given strings X and Y, return a table L such that
    L[j][k] is the length of the Longest Common Subsequence (LCS)
    between X[0..j-1] and Y[0..k-1].
    """
    n, m = len(X), len(Y)

    # Step 1: Initialize DP table of size (n+1) x (m+1) with all zeros
    L = [[0] * (m + 1) for k in range(n + 1)]

    # Step 2: Fill DP table row by row
    for j in range(n):
        for k in range(m):
            # Step 3: If characters match, extend LCS by 1
            if X[j] == Y[k]:
                L[j + 1][k + 1] = L[j][k] + 1
            else:
                # Step 4: Else, take the best from previous rows/cols
                L[j + 1][k + 1] = max(L[j + 1][k], L[j][k + 1])

    return L
# example_X = "AGGTAB"
# example_Y = "GXTXAYB"
# lcs_table = LCS(example_X, example_Y)
# result = lcs_table[-1][-1]  # Length of LCS
# lcs_table would print: 


# ------------------------------------------------------------------------------
# Dynamic Programming Summary

## Key Idea

# Break problems into smaller overlapping subproblems. Store answers to avoid recomputation.

# ---

# ## Matrix Chain Multiplication

# * Input: dimensions d\[0..n], A\[i] is d\[i] x d\[i+1]
# * Goal: minimize scalar multiplications
# * Recurrence:
#   `N[i][j] = min(N[i][k] + N[k+1][j] + d[i]*d[k+1]*d[j+1])`
# * Time: O(n^3)

# ---

# ## Longest Common Subsequence (LCS)

# * Input: strings X and Y
# * Goal: length of longest common subsequence
# * Recurrence:

#   * If match: `L[i][j] = L[i-1][j-1] + 1`
#   * Else: `L[i][j] = max(L[i-1][j], L[i][j-1])`
# * Time: O(n·m)

# ---

# ## Traits of DP

# * Reusable subproblems
# * Best substructure builds full solution

# ---

# ## Summary

# | Problem     | Table     | Time   |
# | ----------- | --------- | ------ |
# | Matrix Mult | N\[i]\[j] | O(n^3) |
# | LCS         | L\[i]\[j] | O(nm)  |
