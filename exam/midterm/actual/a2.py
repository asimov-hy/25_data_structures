from a1 import HeapBase
# Problem a2: Heap Implementation

# Implement the following methods in the `Heap` class:

# - `add(self, key: int)`: This method should insert a new key into the heap. This method returns nothing.

#     Note: The new key should be added at the end of the heap (the next available position in the array) 
#               and then moved up to maintain the heap-order property.

# - `remove_min(self) -> int`: This method should remove and return the minimum key from the heap. 
#                                   It should also maintain the heap-order property after the removal.

#     Note: The minimum key is the root of the heap.
#     Note2: This method should fail if the heap is empty. 
#           (raise an exception, e.g., `raise IndexError()`)

# 오류 발생

class Heap(HeapBase):
    # todo: implement this
    def add(self, value):
        self._data.append(value)
        self._upheap(len(self._data) - 1)

    # todo: implement this
    def remove_min(self):   # 오류? - remove_min 에서 오류 발생 - can't return min_value
        if self.is_empty():
            raise IndexError('the heap is empty.')
        
        self._swap(0, len(self._data) - 1) # put min at the end
        item = self._data.pop()
        self._downheap(0)
        return (item._value)
