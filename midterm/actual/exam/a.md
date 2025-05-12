# Problem a: Heap

(21 points)

A heap is a binary tree storing keys at its nodes and satisfying the following properties:

- Heap-Order: For every internal node `v` other than the root, `key(v) >= key(parent(v))`.
- Complete Binary Tree: let `h` be the height of the heap
    - for `i = 0, ..., h-1` there are `2^i` nodes of depth `i`.
    - at depth `h - 1`, the internal nodes are to the left of the external nodes.

A base structure for the `HeapSkeleton` class is provided for you.

## Problem a1: Up and Down

(Medium, 8 points)

Finish implementing the `HeapBase` class. Currently, the `_upheap` and `_downheap` methods are not fully implemented. Implement these methods to complete the `HeapBase` class.

- `_upheap(self, j: int)`: This method should move the node at index `j` up the heap until the heap-order property is satisfied. This method returns nothing.

- `_downheap(self, j: int)`: This method should move the node at index `j` down the heap until the heap-order property is satisfied. This method returns nothing.

## Problem a2: Heap Implementation

(Medium, 8 points)

Implement the following methods in the `Heap` class:

- `add(self, key: int)`: This method should insert a new key into the heap. This method returns nothing.

    Note: The new key should be added at the end of the heap (the next available position in the array) and then moved up to maintain the heap-order property.

- `remove_min(self) -> int`: This method should remove and return the minimum key from the heap. It should also maintain the heap-order property after the removal.

    Note: The minimum key is the root of the heap.

    Note2: This method should fail if the heap is empty. (raise an exception, e.g., `raise IndexError()`)

## Problem a3: Heap Sort

(Easy, 5 points)

Implement the following function:

- `heap_sort(arr: list[int]) -> list[int]`: This function should take a list of integers as input and return a new list containing the same integers sorted in non-decreasing order. You must use the `Heap` class to implement this function.

    Note: You should not use any built-in sorting functions or libraries. The function should be implemented using the `Heap` class you created in the previous problem.

    Note2: The input list should not be modified. A new sorted list should be returned.
