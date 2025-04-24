class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

#------------------------------------------------------------------------------------

# Recall PQ Sorting
# General PQ-sort using a priority queue (either sorted or unsorted)
# The priority queue is defined with a comparator
# The sorting behavior and time complexity depend on the implementation of the priority queue

# Phase 1: Move all elements from S into priority queue P
# (a) S = (7,4,8,2,5,3,9), P = ()
# (b) S = (4,8,2,5,3,9),   P = (7)
# (c) S = (8,2,5,3,9),     P = (4,7)
# (d) S = (2,5,3,9),       P = (4,7,8)
# (e) S = (5,3,9),         P = (2,4,7,8)
# (f) S = (3,9),           P = (2,4,5,7,8)
# (g) S = (9),             P = (2,3,4,5,7,8)
#     S = (),              P = (2,3,4,5,7,8,9)

# Phase 2: Remove min from P and insert back into S in sorted order
# (a) P = (2,3,4,5,7,8,9), S = ()
# (b) P = (3,4,5,7,8,9),   S = (2)
# (c) P = (4,5,7,8,9),     S = (2,3)
# (d) P = (5,7,8,9),       S = (2,3,4)
# (e) P = (7,8,9),         S = (2,3,4,5)
# (f) P = (8,9),           S = (2,3,4,5,7)
# (g) P = (9),             S = (2,3,4,5,7,8)
#     P = (),              S = (2,3,4,5,7,8,9)

# PQ-Sort (Recall PQ Sorting)
# This implementation can be used with any PriorityQueue (unsorted or sorted)
def pq_sort(S, C):
    P = SortedPriorityQueue(C)  # Can also be UnsortedPriorityQueue()
    
    # Phase 1: Insert all elements from sequence into priority queue
    while not S.is_empty():
        e = S.remove_first()
        P.add(e, e)  # both key and value are the element (e)

    # Phase 2: Remove all elements in sorted order and reinsert into sequence
    while not P.is_empty():
        e = P.remove_min()[0]
        S.add_last(e)

#------------------------------------------------------------------------------------

# heap

class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap."""
    
    #--------------------- nonpublic behaviors ---------------------
    
    def _parent(self, j):
        """Return index of parent of node at index j."""
        return (j - 1) // 2

    def _left(self, j):
        """Return index of left child of node at index j."""
        return 2 * j + 1

    def _right(self, j):
        """Return index of right child of node at index j."""
        return 2 * j + 2

    def _has_left(self, j):
        """Return True if node at index j has a left child."""
        return self._left(j) < len(self._data)  # index must be in bounds

    def _has_right(self, j):
        """Return True if node at index j has a right child."""
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """Swap the elements at indices i and j of the array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        """Move item at index j up the heap to restore heap order."""
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)              # swap with parent
            self._upheap(parent)               # recur at position of parent

    def _downheap(self, j):
        """Move item at index j down the heap to restore heap order."""
        if self._has_left(j):
            left = self._left(j)
            small_child = left                 # assume left child is smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right        # right child is smaller
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)     # swap with smaller child
                self._downheap(small_child)    # recur at position of child

    #--------------------- public behaviors ---------------------

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = []

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(_Item(key, value))      # add new item at the end
        self._upheap(len(self._data) - 1)         # upheap newly added position

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self._swap(0, len(self._data) - 1)         # put minimum item at the end
        item = self._data.pop()                    # remove it from the list
        self._downheap(0)                          # fix new root
        return (item._key, item._value)

#------------------------------------------------------------------------------------
# merging two heaps

class HeapPriorityQueueWithMerge:
    class _Item:
        def __init__(self, key, value=None):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

    def __init__(self):
        self._data = []

    def _parent(self, j): return (j - 1) // 2
    def _left(self, j): return 2 * j + 1
    def _right(self, j): return 2 * j + 2
    def _has_left(self, j): return self._left(j) < len(self._data)
    def _has_right(self, j): return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    def add(self, key, value=None):
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def merge_with_key(self, other_heap, key, value=None):
        """Merge current heap and other_heap under a new root node `key`."""
        new_heap = HeapPriorityQueueWithMerge()
        new_heap._data = [self._Item(key, value)] + self._data + other_heap._data
        new_heap._downheap(0)
        return new_heap

#------------------------------------------------------------------------------------

# bottom up heap construction

def bottom_up_heapify(keys):
    """Constructs a min-heap from an unsorted list of keys using bottom-up approach."""
    class _Item:
        def __init__(self, key): self._key = key
        def __lt__(self, other): return self._key < other._key
        def __repr__(self): return str(self._key)

    heap = [_Item(k) for k in keys]

    def _left(j): return 2 * j + 1
    def _right(j): return 2 * j + 2
    def _has_left(j): return _left(j) < len(heap)
    def _has_right(j): return _right(j) < len(heap)

    def _swap(i, j):
        heap[i], heap[j] = heap[j], heap[i]

    def _downheap(j):
        if _has_left(j):
            left = _left(j)
            small = left
            if _has_right(j):
                right = _right(j)
                if heap[right] < heap[left]:
                    small = right
            if heap[small] < heap[j]:
                _swap(j, small)
                _downheap(small)

    # Start from last internal node and go backward
    start = (len(heap) - 2) // 2
    for j in range(start, -1, -1):
        _downheap(j)

    return [item._key for item in heap]

#------------------------------------------------------------------------------------

# heap sort

def heap_sort(S):
    """Sort the sequence S in nondecreasing order using a HeapPriorityQueue."""
    P = HeapPriorityQueue()
    
    # Phase 1: Insert all elements into the heap
    for element in S:
        P.add(element, element)
    
    # Phase 2: Extract min and rebuild S in sorted order
    S.clear()
    while not P.is_empty():
        S.append(P.remove_min()[1])  # append the value part
