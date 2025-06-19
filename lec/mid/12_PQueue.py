from DoubleList import PositionalList

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

#------------------------------------------------------------------------------------

# Priority Queue Base Class

class PriorityQueueBase:
    """Abstract base class for a priority queue."""
    pass  # Placeholder for future functionality

class _Item:
    """Lightweight composite to store priority queue items."""
    
    __slots__ = '_key', '_value'  # Use __slots__ to save memory by declaring fixed attributes

    def __init__(self, k, v):
        self._key = k      # Store the key used for comparison
        self._value = v    # Store the associated value

    def __lt__(self, other):
        """Compare items based on their keys."""
        return self._key < other._key  # Enables sorting by key

class SomeQueue(PriorityQueueBase):
    def __len__(self):
        """Abstract length method; assumed to be implemented in subclasses."""
        return 0  # Example only; actual implementation would depend on subclass logic

    def is_empty(self):
        """Return True if the priority queue is empty."""
        return len(self) == 0

#------------------------------------------------------------------------------------

# Unsorted list implementation of a priority queue
# add takes O(1) time since we can insert the item at the beginning or end of the sequence
# min takes O(n) time, remove_min takes O(n) time since we need to find the minimum item in the list

class UnsortedPriorityQueue(PriorityQueueBase):
    # Inherits from PriorityQueueBase, which provides _Item and is_empty
    """A min-oriented priority queue implemented with an unsorted list."""

    def _find_min(self):  # nonpublic utility
        """Return Position of item with minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty')  # Use base class exception
        
        small = self._data.first()  # Assume the first item is the smallest for now
        walk = self._data.after(small)  # Start checking from the second item

        while walk is not None:
            if walk.element() < small.element():  # Compare based on key via _Item.__lt__
                small = walk  # Update smallest if a smaller key is found
            walk = self._data.after(walk)  # Move to next position

        return small  # Return the position of the smallest item

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()  # Use a positional list to store the items

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        self._data.add_last(_Item(key, value))  # Append to the list
        # self._data.add_last(self._Item(key, value))  # Append to the list

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        p = self._find_min()         # Find position of the smallest item
        item = p.element()           # Get the actual _Item object
        return (item._key, item._value)  # Return key-value pair

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        p = self._find_min()                   # Find the position of the smallest item
        item = self._data.delete(p)            # Remove it from the list
        return (item._key, item._value)        # Return key-value pair

#------------------------------------------------------------------------------------

# Sorted list implementation of a priority queue
# add takes O(n) time since we need to find the right position to insert the item
# min takes O(1) time since we can just return the first item in the list
# remove_min takes O(1) time since we can just remove the first item in the list


class SortedPriorityQueue(PriorityQueueBase):
    # base class defines _Item
    """A min-oriented priority queue implemented with a sorted list."""

    def __init__(self, comparator = lambda x, y: x<y):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()  # Use a positional list to store sorted items
        self._comp = comparator # added for priority queue sorting

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        newest = _Item(key, value)  # Create a new _Item to insert
        walk = self._data.last()    # Start from the last position in the list

        # Walk backward as long as the current item is greater than the one we're inserting
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)

        if walk is None:
            # New key is the smallest; insert at the front
            self._data.add_first(newest)
        else:
            # Insert after the position with a smaller (or equal) key
            self._data.add_after(walk, newest)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty.')

        p = self._data.first()         # First item is the one with the minimum key
        item = p.element()             # Get the _Item at that position
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty.')

        # Remove the first position (smallest key)
        item = self._data.delete(self._data.first())
        return (item._key, item._value)


#------------------------------------------------------------------------------------

# Priority Queue sorting
# inserts the elements one by one into the queue and then removes them in sorted order
# Remove the elements in sorted order with a series of remove_min operations

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

def pq_sort(S, C):
    """
    Input:  sequence S, comparator C
    Output: S sorted in increasing order by C
    """
    P = SortedPriorityQueue(C)  # P ← priority queue with comparator C

    while not S.is_empty():      # while ¬S.is_empty()
        e = S.remove_first()     # e ← S.remove_first()
        P.add(e, None)           # P.add(e, ∅)

    while not P.is_empty():      # while ¬P.is_empty()
        e = P.remove_min()[0]    # e ← P.removeMin().key()
        S.add_last(e)            # S.add_last(e)

#------------------------------------------------------------------------------------

# Selection sort
# variation of PQ-sort where the priority queue is implemented with an unsorted sequence

# Phase 1: Move all elements from S into priority queue P
# (a) S = (7,4,8,2,5,3,9), P = ()
# (b) S = (4,8,2,5,3,9),   P = (7)
# (c) S = (8,2,5,3,9),     P = (7,4)
# (d) S = (2,5,3,9),       P = (7,4,8)
# (e) S = (5,3,9),         P = (7,4,8,2)
# (f) S = (3,9),           P = (7,4,8,2,5)
# (g) S = (9),             P = (7,4,8,2,5,3)
#     S = (),              P = (7,4,8,2,5,3,9)

# Phase 2: Remove min from P and insert back into S in sorted order
# (a) P = (7,4,8,2,5,3,9), S = ()
# (b) P = (7,4,8,5,3,9),   S = (2)
# (c) P = (7,4,8,5,9),     S = (2,3)
# (d) P = (7,8,5,9),       S = (2,3,4)
# (e) P = (7,8,9),         S = (2,3,4,5)
# (f) P = (8,9),           S = (2,3,4,5,7)
# (g) P = (9),             S = (2,3,4,5,7,8)
#     P = (),              S = (2,3,4,5,7,8,9)

# Sequence wrapper (as used in pq_sort)
class Sequence:
    """
    A simple wrapper class for a sequence (list) to demonstrate priority queue sorting.
    Purpose: Provides basic operations for adding, removing, and checking elements in a sequence.
    """

    def __init__(self, data):
        # Initialize the sequence with a list of data
        self._data = list(data)

    def is_empty(self):
        # Check if the sequence is empty
        return len(self._data) == 0

    def remove_first(self):
        # Remove and return the first element of the sequence
        return self._data.pop(0)

    def add_last(self, e):
        # Add an element to the end of the sequence
        self._data.append(e)

    def __repr__(self):
        # Return a string representation of the sequence
        return repr(self._data)

    def get(self):
        # Return a copy of the sequence for printing or external use
        return list(self._data)

# Selection Sort (PQ-Sort with UnsortedPriorityQueue)
def selection_sort(S):
    P = UnsortedPriorityQueue()
    while not S.is_empty():
        e = S.remove_first()
        P.add(e)
    while not P.is_empty():
        e = P.remove_min()._key
        S.add_last(e)


#------------------------------------------------------------------------------------

# Insertion Sort
# Variation of PQ-Sort where the priority queue is implemented with a **sorted sequence**
# Insertions are O(n), removals are O(1)
# Total time complexity: O(n²)

# Phase 1: Move all elements from S into priority queue P (which maintains sorted order)
# (a) S = (7,4,8,2,5,3,9), P = ()
# (b) S = (4,8,2,5,3,9),   P = (7)
# (c) S = (8,2,5,3,9),     P = (4,7)
# (d) S = (2,5,3,9),       P = (4,7,8)
# (e) S = (5,3,9),         P = (2,4,7,8)
# (f) S = (3,9),           P = (2,4,5,7,8)
# (g) S = (),              P = (2,3,4,5,7,8,9)

# Phase 2: Remove min from P and insert back into S in sorted order
# (a) P = (3,4,5,7,8,9),   S = (2)
# (b) P = (),              S = (2,3,4,5,7,8,9)

# Insertion Sort = PQ-Sort using SortedPriorityQueue with tracing
def insertion_sort(S, C):
    P = SortedPriorityQueue(C)
    while not S.is_empty():
        e = S.remove_first()
        P.add(e, None)
    while not P.is_empty():
        e = P.remove_min()[0]
        S.add_last(e)


#------------------------------------------------------------------------------------

# Insertion Sort (in-place)

def in_place_insertion_sort(A):
    """
    Sorts the input list A in-place using the insertion sort algorithm.
    Follows the diagram where:
    - The left portion is maintained sorted.
    - Values are shifted to the right to insert the current element.
    """
    n = len(A)
    print("Initial:", A)
    for i in range(1, n):
        current = A[i]
        j = i
        # Shift larger elements to the right
        while j > 0 and A[j - 1] > current:
            A[j] = A[j - 1]
            j -= 1
        A[j] = current
        print(f"Step {i}:  {A}")
