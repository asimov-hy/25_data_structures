import random

class SkipListNode:
    """A node in the skip list."""
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)  # list of forward pointers

class SkipList:
    """Skip list data structure."""
    MAX_LEVEL = 16  # maximum number of levels

    def __init__(self):
        self.header = SkipListNode(None, SkipList.MAX_LEVEL)
        self.level = 0

    def random_level(self):
        lvl = 0
        while random.random() < 0.5 and lvl < SkipList.MAX_LEVEL:
            lvl += 1
        return lvl

    def insert(self, key):
        update = [None] * (SkipList.MAX_LEVEL + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]
        if current is None or current.key != key:
            lvl = self.random_level()
            if lvl > self.level:
                for i in range(self.level + 1, lvl + 1):
                    update[i] = self.header
                self.level = lvl

            new_node = SkipListNode(key, lvl)
            for i in range(lvl + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, key):
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.key == key:
            return current
        return None

    def delete(self, key):
        update = [None] * (SkipList.MAX_LEVEL + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]
        if current and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1

# Sample skip list for testing
skiplist = SkipList()
for key in [3, 6, 7, 9, 12, 19, 21, 25, 26]:
    skiplist.insert(key)

found_node = skiplist.search(19)
not_found_node = skiplist.search(20)
(skiplist.level, found_node.key if found_node else None, not_found_node)
