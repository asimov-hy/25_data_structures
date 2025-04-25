class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression"""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map"""
        self._table = ca[ *[None]]  # Initialize the hash table with None values (syntax error here)
        self._n = 0  # Initialize the number of elements in the hash table
        self._prime = p  # Prime number used for MAD compression
        self._scale = 1 + randrange(p - 1)  # Random scale factor for MAD compression
        self._shift = randrange(p)  # Random shift factor for MAD compression

    def _hash_function(self, k):
        """Compute hash value for key k using MAD compression"""
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        """Return the number of elements in the hash table"""
        return self._n

    def __getitem__(self, k):
        """Retrieve the value associated with key k"""
        k = self._hash_function(k)  # Compute the hash index for key k
        return self._bucket_getitem(j, k)  # Retrieve the value from the appropriate bucket

    def __setitem__(self, k, v):
        """Insert or update the value associated with key k"""
        j = self._hash_function(k)  # Compute the hash index for key k
        self._bucket_setitem(j, k, v)  # Insert or update the key-value pair in the bucket
        if self._n > len(self._table) // 2:  # Check if resizing is needed
            self._resize(2 * len(self._table) - 1)  # Resize the table to double its size

    def __delitem__(self, k):
        """Remove the item associated with key k"""
        j = self._hash_function(k)  # Compute the hash index for key k
        self._bucket_delitem(j, k)  # Remove the key-value pair from the bucket
        self._n -= 1  # Decrement the number of elements

    def _resize(self, c):
        """Resize the hash table to a new capacity c"""
        old = list(self.items())  # Copy all existing items
        self._table = c * [None]  # Create a new table with the new capacity
        self._n = 0  # Reset the number of elements
        for (k, v) in old:  # Reinsert all items into the new table
            self[k] = v

#--------------------------------------------------

# Hash table with separate chaining

class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""

    def _bucket_getitem(self, j, k):
        """Get item with key k from bucket at index j."""
        bucket = self._table[j]  # Retrieve the bucket at index j
        if bucket is None:  # If the bucket is empty
            raise KeyError('Key Error: ' + repr(k))  # No match found
        return bucket[k]  # Retrieve the value associated with key k

    def _bucket_setitem(self, j, k, v):
        """Set item with key k to value v in bucket at index j."""
        if self._table[j] is None:  # If the bucket is empty
            self._table[j] = UnsortedTableMap()  # Create a new bucket
        oldsize = len(self._table[j])  # Record the current size of the bucket
        self._table[j][k] = v  # Insert or update the key-value pair
        if len(self._table[j]) > oldsize:  # If a new key was added
            self._n += 1  # Increment the total number of elements

    def _bucket_delitem(self, j, k):
        """Remove item with key k from bucket at index j."""
        bucket = self._table[j]  # Retrieve the bucket at index j
        if bucket is None:  # If the bucket is empty
            raise KeyError('Key Error: ' + repr(k))  # No match found
        del bucket[k]  # Remove the key-value pair

    def __iter__(self):
        """Generate iteration of all keys in the map."""
        for bucket in self._table:  # Iterate through all buckets
            if bucket is not None:  # If the bucket is not empty
                for key in bucket:  # Iterate through all keys in the bucket
                    yield key  # Yield each key

#--------------------------------------------------

# Hash table with linear probing

class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution."""

    _AVAIL = object()  # Sentinel to mark locations of previous deletions

    def _is_available(self, j):
        """Return True if index j is available in table."""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """
        Search for key k in bucket at index j.
        Return (success, index) tuple:
        - If match was found: (True, index of match)
        - If not found:       (False, index of first available slot)
        """
        firstAvail = None  # Initialize the first available slot
        while True:  # Loop until a match is found or the search fails
            if self._is_available(j):  # If the slot is available
                if firstAvail is None:  # If this is the first available slot
                    firstAvail = j  # Mark this as the first available slot
                if self._table[j] is None:  # If the slot is empty
                    return (False, firstAvail)  # Search failed
            elif k == self._table[j]._key:  # If the key matches
                return (True, j)  # Match found
            j = (j + 1) % len(self._table)  # Move to the next slot (wrap around)

    def _bucket_getitem(self, j, k):
        """Retrieve value associated with key k at bucket index j."""
        found, s = self._find_slot(j, k)  # Find the slot for key k
        if not found:  # If no match was found
            raise KeyError('Key Error: ' + repr(k))  # Raise a KeyError
        return self._table[s]._value  # Return the value associated with key k

    def _bucket_setitem(self, j, k, v):
        """Assign value v to key k at bucket index j."""
        found, s = self._find_slot(j, k)  # Find the slot for key k
        if not found:  # If no match was found
            self._table[s] = self._Item(k, v)  # Insert a new key-value pair
            self._n += 1  # Increment the number of elements
        else:  # If a match was found
            self._table[s]._value = v  # Update the value for the existing key

    def _bucket_delitem(self, j, k):
        """Remove item associated with key k at bucket index j."""
        found, s = self._find_slot(j, k)  # Find the slot for key k
        if not found:  # If no match was found
            raise KeyError('Key Error: ' + repr(k))  # Raise a KeyError
        self._table[s] = ProbeHashMap._AVAIL  # Mark the slot as vacated

    def __iter__(self):
        """Iterate through all keys in the map."""
        for j in range(len(self._table)):  # Iterate through all slots in the table
            if not self._is_available(j):  # If the slot is not available
                yield self._table[j]._key  # Yield the key in the slot
