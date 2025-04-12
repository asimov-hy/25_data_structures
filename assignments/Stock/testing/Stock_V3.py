class stock_manager:

    class _Stock:
        __slots__ = '_price', '_quantity'

        def __init__(self, price, quantity):
            self._price = price
            self._quantity = quantity

        def __lt__(self, other):
            return self._price < other._price

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def add(self, price, quantity):
        newest = self._Stock(price, quantity)
        index = len(self._data)
        while index > 0 and newest < self._data[index - 1]:
            index -= 1
        self._data.insert(index, newest)

    def min(self):
        if self.is_empty():
            raise Exception("Priority queue is empty.")
        item = self._data[0]
        return (item._price, item._quantity)

    def remove_min(self):
        if self.is_empty():
            raise Exception("Priority queue is empty.")
        item = self._data.pop(0)
        return (item._price, item._quantity)

