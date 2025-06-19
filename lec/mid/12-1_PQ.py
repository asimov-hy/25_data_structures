class PriorityQueue:
    """A simple min-priority queue without using heapq."""
    def __init__(self):
        self._queue = []  # List of tuples: (priority, item)

    def push(self, priority, item):
        """Insert an item into the queue with the given priority."""
        entry = (priority, item)
        inserted = False
        for i in range(len(self._queue)):
            if priority < self._queue[i][0]:  # Lower number = higher priority
                self._queue.insert(i, entry)
                inserted = True
                break
        if not inserted:
            self._queue.append(entry)

    def pop(self):
        """Remove and return the item with the highest priority (lowest number)."""
        if self.is_empty():
            raise IndexError("pop from empty priority queue")
        return self._queue.pop(0)[1]

    def peek(self):
        """Return the item with the highest priority without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        return self._queue[0][1]

    def is_empty(self):
        return len(self._queue) == 0

    def __len__(self):
        return len(self._queue)

#-----------------------------------------------

# selection sort

def selection_sort(arr):
    """Sorts the list in ascending order using selection sort."""
    n = len(arr)
    for i in range(n):
        min_index = i
        # Find the index of the smallest element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

#-----------------------------------------------

# insertion sort

def insertion_sort(arr):
    """Sorts the list in ascending order using insertion sort."""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#-----------------------------------------------

# in-place insertion sort

def insertion_sort_in_place(arr):
    """Sorts the list in ascending order using in-place insertion sort."""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key