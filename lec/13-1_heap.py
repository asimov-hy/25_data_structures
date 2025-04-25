class MinHeap:
    """A simple binary min-heap."""
    # min heap is a complete binary tree where the value of each node is less than or equal to the values of its children.
    def __init__(self):
        # Initialize an empty list to store heap elements
        self._heap = []

    def push(self, value):
        """Add a new value to the heap."""
        # Append the new value to the end of the heap
        self._heap.append(value)
        # Restore the heap property by moving the new value up
        self._heapify_up(len(self._heap) - 1)

    def pop(self):
        """Remove and return the smallest value (root)."""
        if self.is_empty():
            # Raise an error if the heap is empty
            raise IndexError("pop from empty heap")
        # Store the smallest value (root) to return later
        min_value = self._heap[0]
        # Remove the last element from the heap
        last = self._heap.pop()
        if self._heap:
            # Move the last element to the root
            self._heap[0] = last
            # Restore the heap property by moving the root element down
            self._heapify_down(0)
        return min_value

    def peek(self):
        """Return the smallest value without removing it."""
        if self.is_empty():
            # Raise an error if the heap is empty
            raise IndexError("peek from empty heap")
        # Return the root element (smallest value)
        return self._heap[0]

    def is_empty(self):
        # Check if the heap is empty
        return len(self._heap) == 0

    def _heapify_up(self, index):
        """Move the element at index up to restore heap property."""
        # Calculate the parent index
        parent = (index - 1) // 2
        # If the current element is smaller than its parent, swap them
        if index > 0 and self._heap[index] < self._heap[parent]:
            self._heap[index], self._heap[parent] = self._heap[parent], self._heap[index]
            # Recursively heapify up the parent
            self._heapify_up(parent)

    def _heapify_down(self, index):
        """Move the element at index down to restore heap property."""
        # Assume the current index is the smallest
        smallest = index
        # Calculate the indices of the left and right children
        left = 2 * index + 1
        right = 2 * index + 2
        # Get the size of the heap
        n = len(self._heap)

        # Check if the left child exists and is smaller than the current smallest
        if left < n and self._heap[left] < self._heap[smallest]:
            smallest = left
        # Check if the right child exists and is smaller than the current smallest
        if right < n and self._heap[right] < self._heap[smallest]:
            smallest = right
        # If the smallest element is not the current index, swap and continue heapifying down
        if smallest != index:
            self._heap[index], self._heap[smallest] = self._heap[smallest], self._heap[index]
            self._heapify_down(smallest)

# max heap

class MaxHeap:
    """A simple binary max-heap."""
    def __init__(self):
        # Initialize an empty list to store heap elements
        self._heap = []

    def push(self, value):
        """Add a new value to the heap."""
        # Append the new value to the end of the heap
        self._heap.append(value)
        # Restore the heap property by moving the new value up
        self._heapify_up(len(self._heap) - 1)

    def pop(self):
        """Remove and return the largest value (root)."""
        if self.is_empty():
            # Raise an error if the heap is empty
            raise IndexError("pop from empty heap")
        # Store the largest value (root) to return later
        max_value = self._heap[0]
        # Remove the last element from the heap
        last = self._heap.pop()
        if self._heap:
            # Move the last element to the root
            self._heap[0] = last
            # Restore the heap property by moving the root element down
            self._heapify_down(0)
        return max_value

    def peek(self):
        """Return the largest value without removing it."""
        if self.is_empty():
            # Raise an error if the heap is empty
            raise IndexError("peek from empty heap")
        # Return the root element (largest value)
        return self._heap[0]

    def is_empty(self):
        # Check if the heap is empty
        return len(self._heap) == 0

    def _heapify_up(self, index):
        """Move the element at index up to restore heap property."""
        # Calculate the parent index
        parent = (index - 1) // 2
        # If the current element is larger than its parent, swap them
        if index > 0 and self._heap[index] > self._heap[parent]:
            self._heap[index], self._heap[parent] = self._heap[parent], self._heap[index]
            # Recursively heapify up the parent
            self._heapify_up(parent)

    def _heapify_down(self, index):
        """Move the element at index down to restore heap property."""
        # Assume the current index is the largest
        largest = index
        # Calculate the indices of the left and right children
        left = 2 * index + 1
        right = 2 * index + 2
        # Get the size of the heap
        n = len(self._heap)

        # Check if the left child exists and is larger than the current largest
        if left < n and self._heap[left] > self._heap[largest]:
            largest = left
        # Check if the right child exists and is larger than the current largest
        if right < n and self._heap[right] > self._heap[largest]:
            largest = right
        # If the largest element is not the current index, swap and continue heapifying down
        if largest != index:
            self._heap[index], self._heap[largest] = self._heap[largest], self._heap[index]
            self._heapify_down(largest)

#-------------

def heap_sort(arr):
    """Sort the array in ascending order using a max-heap."""
    n = len(arr)

    # Build max heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current max to end
        _heapify(arr, i, 0)              # Restore heap property

def _heapify(arr, n, i):
    """Ensure subtree rooted at index i is a max-heap (heapify down)."""
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
