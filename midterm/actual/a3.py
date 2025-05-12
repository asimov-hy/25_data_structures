from a2 import Heap
# Problem a3: Heap Sort

# (Easy, 5 points)

# Implement the following function:

# - `heap_sort(arr: list[int]) -> list[int]`: This function should take a list of integers as input 
#                                               and return a new list containing the same integers sorted in non-decreasing order. 
#                                               You must use the `Heap` class to implement this function.

# class Heap(HeapBase):
#     # todo: implement this
#     def add(self, value):
#         self._data.append(value)
#         self._upheap(len(self._data) - 1)

#     # todo: implement this
#     def remove_min(self):   # 오류? - remove_min 에서 오류 발생 - can't return min_value
#         if self.is_empty():
#             raise IndexError('the heap is empty.')
        
#         self._swap(0, len(self._data) - 1) # put min at the end
#         item = self._data.pop()
#         self._downheap(0)
#         return (item._value)

#     Note: You should not use any built-in sorting functions or libraries. 
#           The function should be implemented using the `Heap` class you created in the previous problem.

#     Note2: The input list should not be modified. A new sorted list should be returned.

# todo: implement this
def heap_sort(arr):
    n = len(arr)

    # Build max heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current max to end
        _heapify(arr, i, 0)              # Restore heap property

#-------------------------------------------------------------

def _heapify(arr, n, i):
    largest = i
    left = 2 * i + 1     # Left child index
    right = 2 * i + 2    # Right child index

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)