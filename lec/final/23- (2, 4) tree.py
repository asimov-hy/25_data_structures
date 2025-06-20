"""
Tree24 (2-4 Tree) Implementation
-------------------------------
- Multi-way balanced search tree.
- Each node holds 1–3 sorted keys, 0–4 children.
- All leaves are at the same depth.

Supports:
- insert(key): Adds key to correct leaf, splits if overfull.
- search(key): Recursively finds key or returns None.

Overflow Handling:
- Split node on 4 keys.
- Promote middle key to parent.
- Split may propagate up; new root created if needed.

Maintains:
- Logarithmic height.
- Sorted order.
- Automatic balance via key promotion.
"""


class Tree24:
    class Node:
        def __init__(self, parent=None):
            self.keys = []          # Holds 1 to 3 keys
            self.children = []      # Holds 0 to 4 children
            self.parent = parent    # Pointer to parent node

        def is_leaf(self):
            # Returns True if node has no children
            return len(self.children) == 0

        def is_overflow(self):
            # Returns True if node has more than 3 keys
            return len(self.keys) > 3

        def insert_key(self, key):
            # Inserts a key and keeps the list sorted
            self.keys.append(key)
            self.keys.sort()

    def __init__(self):
        # Initialize the tree with a single root node
        self.root = self.Node()

    def search(self, key, node=None):
        # Public search method (recursive)
        if node is None:
            node = self.root

        # 1. Search through keys in current node
        for i, item in enumerate(node.keys):
            if key == item:
                return node  # Found
            elif key < item:
                # 2. Go left child
                if node.is_leaf():
                    return None
                return self.search(key, node.children[i])

        # 3. Go rightmost child
        if node.is_leaf():
            return None
        return self.search(key, node.children[-1])

    def insert(self, key):
        # Insert a key into the tree
        node = self.root

        # 1. Traverse to the correct leaf
        while not node.is_leaf():
            for i, item in enumerate(node.keys):
                if key < item:
                    node = node.children[i]
                    break
            else:
                node = node.children[-1]

        # 2. Insert the key into the leaf node
        node.insert_key(key)

        # 3. Fix overflow if node exceeds 3 keys
        self._fix_overflow(node)

    def _fix_overflow(self, node):
        # Rebalance upward if a node overflows
        while node and node.is_overflow():
            mid_index = 2
            mid_key = node.keys[mid_index]

            # 1. Create left and right split nodes
            left = self.Node()
            right = self.Node()

            left.keys = node.keys[:mid_index]
            right.keys = node.keys[mid_index + 1:]

            # 2. If node has children, divide them between splits
            if node.children:
                left.children = node.children[:3]
                right.children = node.children[3:]
                for child in left.children:
                    child.parent = left
                for child in right.children:
                    child.parent = right

            # 3. Handle root overflow
            if node == self.root:
                self.root = self.Node()
                self.root.keys = [mid_key]
                self.root.children = [left, right]
                left.parent = right.parent = self.root
                return
            else:
                parent = node.parent
                insert_index = parent.children.index(node)

                # 4. Promote mid_key to parent
                parent.keys.append(mid_key)
                parent.keys.sort()

                # 5. Replace old child with two new ones
                parent.children.pop(insert_index)
                parent.children.insert(insert_index, left)
                parent.children.insert(insert_index + 1, right)
                left.parent = right.parent = parent

                # 6. Move up to parent
                node = parent
