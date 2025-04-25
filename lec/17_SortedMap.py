# binary search

def binary_search(data, target, low, high):
    """
    Return True if target is found in the portion of the list from data[low] to data[high], inclusive.
    Uses recursive binary search.
    """
    if low > high:
        return False                     # Base case: interval is empty, no match
    else:
        mid = (low + high) // 2          # Calculate midpoint
        if target == data[mid]:
            return True                  # Match found
        elif target < data[mid]:
            # Search left half
            return binary_search(data, target, low, mid - 1)
        else:
            # Search right half
            return binary_search(data, target, mid + 1, high)

#------------------------------------------------------------------------------------

# sorted map implementation

class SortedTableMap(MapBase):
    """Map implementation using a sorted table."""

    # ------------------------ nonpublic behaviors ------------------------
    def _find_index(self, k, low, high):
        """Return index of the leftmost item with key >= k using binary search."""
        if high < low:
            return high + 1  # No element qualifies
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid  # Found exact match
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1)  # Search left
            else:
                return self._find_index(k, mid + 1, high)  # Search right

    # ------------------------ public behaviors ------------------------
    def __init__(self):
        """Create an empty map."""
        self._table = []

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[j]._value

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value = v  # Reassign
        else:
            self._table.insert(j, self._Item(k, v))  # Add new item

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(j)

    def __iter__(self):
        """Generate keys of the map ordered from minimum to maximum."""
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """Generate keys of the map ordered from maximum to minimum."""
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        """Return (key, value) pair with minimum key (or None if empty)."""
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        """Return (key, value) pair with maximum key (or None if empty)."""
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_le(self, k):
        """Return (key, value) pair with greatest key less than or equal to k."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            return (self._table[j]._key, self._table[j]._value)
        elif j > 0:
            return (self._table[j - 1]._key, self._table[j - 1]._value)
        else:
            return None

    def find_lt(self, k):
        """Return (key, value) pair with greatest key strictly less than k."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j > 0:
            return (self._table[j - 1]._key, self._table[j - 1]._value)
        else:
            return None

    def find_ge(self, k):
        """Return (key, value) pair with least key greater than or equal to k."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_gt(self, k):
        """Return (key, value) pair with least key strictly greater than k."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j + 1 < len(self._table):
            return (self._table[j + 1]._key, self._table[j + 1]._value)
        else:
            return None

    def find_range(self, start, stop):
        """Iterate all (key, value) pairs such that start <= key < stop."""
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table) - 1)

        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1
