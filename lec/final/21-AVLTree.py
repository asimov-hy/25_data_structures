class AVLNode:
    def __init__(self, key, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent
        self.height = 1  # New node is initially height 1

class AVL:
    def __init__(self):
        self.root = None

# --------------------------- search ---------------------------

    def search(self, search_node):
        # 1. Set current node
        node = self.root
        # 2. Begin traversal
        while node:
            # 3. If match found
            if search_node == node.key:
                return node
            # 4. If search_node is smaller, go left
            if search_node < node.key:
                node = node.left
            # 5. If search_node is larger, go right
            else:
                node = node.right
        # 6. Not found
        return None

# --------------------------- insert ---------------------------

    def insert(self, target):
        # 1. If tree is empty, insert at root
        if not self.root:
            self.root = AVLNode(target)
            return

        # 2. Recursive insertion function
        def traverse_and_insert(node, parent):
            # 2-1. If position found, create and return new node
            if not node:
                return AVLNode(target, parent)

            # 2-2. Traverse left if target is smaller
            if target < node.key:
                node.left = traverse_and_insert(node.left, node)

            # 2-3. Traverse right if target is larger or equal
            else:
                node.right = traverse_and_insert(node.right, node)

            # 3. Update height of current node
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

            # 4. Rebalance current node if unbalanced
            return self._rebalance(node)

        # 5. Start recursion and re-assign root in case it changes
        self.root = traverse_and_insert(self.root, None)

        self.root.parent = None




# --------------------------- delete ---------------------------

    def delete(self, target):
        # 1. Start recursive deletion
        def traverse_and_delete(node):
            # 1-1. Base case: node not found
            if not node:
                return None

            # 1-2. Traverse left if target is smaller
            if target < node.key:
                node.left = traverse_and_delete(node.left)

            # 1-3. Traverse right if target is larger
            elif target > node.key:
                node.right = traverse_and_delete(node.right)

            # 1-4. Found the node to delete
            else:
                # 1-4-1. Node has only one child or no children
                if not node.left:
                    if node.right:
                        node.right.parent = node.parent
                    return node.right
                elif not node.right:
                    if node.left:
                        node.left.parent = node.parent
                    return node.left

                # 1-4-2. Node has two children
                # Find in-order successor (smallest in right subtree)
                successor = self._min_value_node(node.right)

                # Copy successor's key into current node
                node.key = successor.key

                # Recursively delete the successor
                node.right = traverse_and_delete(node.right)

            # 2. Update height after deletion
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

            # 3. Rebalance current node if needed
            return self._rebalance(node)

        # 4. Start traversal and update root in case it changes
        self.root = traverse_and_delete(self.root)

        if self.root:
            self.root.parent = None


# --------------------------- rebalancing ---------------------------

    def _rebalance(self, node):
        balance = self._get_balance(node)

        # Left heavy
        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right heavy
        if balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Rotate
        y.left = z
        z.right = T2

        # Update parents
        y.parent = z.parent
        z.parent = y
        if T2:
            T2.parent = z

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        # Rotate
        y.right = z
        z.left = T3

        # Update parents
        y.parent = z.parent
        z.parent = y
        if T3:
            T3.parent = z

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

# --------------------------- helpers ---------------------------

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right)

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node