# double strategy array list

import ctypes
# import cytpes for low-level array manipulation

class DynamicArray:
    """ A dynamic array class skin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self.n = 0                                      # number of elements in the array
        self.capacity = 1                               # default array capacity
        self._A = self._make_array(self.capacity)       # low-level array

    def __len__(self):
        """Return number of elements store in the array."""
        return self._n                          # number of elements currently stored = self.n
    
    def __getitem__(self, k):                   # special method to get item at index k
        """Return element at index k."""
        if not 0 <= k < self._n:                # if index k is out of bounds (below 0 or above n-1)
            raise IndexError('invalid index')   # raise exception
        return self._A[k]                       # else retrieve from array
        
    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:           # number of elements = capacity
            self._resize( 2 * self._capacity)   # double capacity     if incremental strategy: self._resize(self._capacity + 1)
        self._A[self._n] = obj              # set next available index(which is A[n]) to obj - n+1 is not used since 0 based index
        self._n += 1                        # increment number of elements in the array

    def _resize(self, c):                       # nonpublic utility when called in _append
        """Resize internal array to capacity c"""
        B = self._make_array(c)                 # create new (bigger) array
        for k in range(self._n):                # copy elements to new array
            B[k] = self._A[k]
        self._A = B                             # update to new array
        self._capacity = c                      # update capacity

    def _make_array(self, c):                   # non public utility when called in _resize
        """Return new array with capacity c."""
        return (c*ctypes.py_object)()           # see ctypes documentation