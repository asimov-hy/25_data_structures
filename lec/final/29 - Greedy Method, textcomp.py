# # Greedy Method Summary

# ## Core Idea

# A greedy algorithm builds a solution step-by-step by choosing the locally optimal choice at each step.

# ### Conditions for correctness:

# * Greedy-choice property
# * Optimal substructure

# ---

# ## Problems Solved with Greedy

# ### 1. Huffman Encoding

# * Goal: Minimize total bits for encoding text
# * Approach: Combine two least frequent trees repeatedly using a min-heap
# * Time: O(n + d log d), where d = number of distinct characters

# ### 2. Fractional Knapsack

# * Goal: Maximize value under weight limit (allowing fractions)
# * Strategy: Sort by value/weight ratio, take highest first
# * Time: O(n log n)

# ### 3. Task Scheduling

# * Goal: Use fewest machines to schedule non-overlapping tasks
# * Strategy: Sort by start time, assign to earliest available slot

# ---

# ## Where Greedy Fails

# ### 1. 0/1 Knapsack

# * Can't take fractions, so greedy choices can miss optimal sets

# ### 2. Coin Change

# * Greedy fails if denominations don't align well (e.g., \[1,3,4] for 6)

# ---
