class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """A locator-based priority queue implemented with a binary heap."""

    # nested Locator class
    class Locator(HeapPriorityQueue._Item):
        """Token for locating an entry of the priority queue."""
        __slots__ = '_index'  # Use __slots__ to save memory by limiting attributes

        def __init__(self, k, v, j):
            super().__init__(k, v)  # Initialize the key and value using the parent class
            self._index = j  # Store the index of the item in the heap

    # nonpublic behaviors
    # override swap to record new indices
    def _swap(self, i, j):
        super()._swap(i, j)  # Perform the swap in the array
        self._data[i]._index = i  # Update the index of the item at position i
        self._data[j]._index = j  # Update the index of the item at position j

    def _bubble(self, j):
        # Check if the item is smaller than its parent and perform upheap if necessary
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)  # Move the item up the heap
        else:
            self._downheap(j)  # Otherwise, move the item down the heap

    # public behaviors
    def add(self, key, value):
        """Add a key-value pair"""
        # Create a new locator with the given key, value, and current index
        token = self.Locator(key, value, len(self._data))
        self._data.append(token)  # Add the locator to the heap
        self._upheap(len(self._data) - 1)  # Restore the heap property by upheaping
        return token  # Return the locator

    def update(self, loc, newkey, newval):
        """Update the key and value of the entry represented by loc."""
        j = loc._index  # Get the index of the locator
        # Validate that the locator is valid and still in the heap
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')  # Raise an error if invalid
        loc._key = newkey  # Update the key of the locator
        loc._value = newval  # Update the value of the locator
        self._bubble(j)  # Restore the heap property by bubbling

    def remove(self, loc):
        """Remove and return the (k, v) pair identified by Locator loc"""
        j = loc._index  # Get the index of the locator
        # Validate that the locator is valid and still in the heap
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')  # Raise an error if invalid
        if j == len(self) - 1:  # If the item is at the last position
            self._data.pop()  # Remove the last item
        else:
            self._swap(j, len(self) - 1)  # Swap the item with the last item
            self._data.pop()  # Remove the last item
            self._bubble(j)  # Restore the heap property by bubbling
        return (loc._key, loc._value)  # Return the key-value pair of the removed item