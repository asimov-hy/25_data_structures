#### DO NOT MODIFY ####
class HeapSkeleton():
    def __init__(self):
        self._data = []

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def is_empty(self):
        return len(self._data) == 0

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return len(self._data)

    def _from_arr(self, arr):
        self._data = arr

    def _upheap(self, j):
        raise NotImplementedError("Must be implemented in subclass")

    def _downheap(self, j):
        raise NotImplementedError("Must be implemented in subclass")

    def add(self, value):
        raise NotImplementedError("Must be implemented in subclass")

    def remove_min(self):
        raise NotImplementedError("Must be implemented in subclass")
