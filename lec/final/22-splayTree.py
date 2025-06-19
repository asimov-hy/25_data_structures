# based on binary search tree

    def _splay(self, node):
        # Repeatedly move the node up to the root
        while node.parent:
            parent = node.parent
            grand = parent.parent

            # 1. Zig case (node's parent is root)
            if not grand:
                # 1-1. Node is left child → single right rotation
                if node == parent.left:
                    self._rotate_right(parent)
                # 1-2. Node is right child → single left rotation
                else:
                    self._rotate_left(parent)

            # 2. Zig-zig case (node and parent are on the same side)
            # 2-1. Node is left child of parent, and parent is left child of grandparent
            elif node == parent.left and parent == grand.left:
                # Perform two right rotations
                self._rotate_right(grand)
                self._rotate_right(parent)

            # 2-2. Node is right child of parent, and parent is right child of grandparent
            elif node == parent.right and parent == grand.right:
                # Perform two left rotations
                self._rotate_left(grand)
                self._rotate_left(parent)

            # 3. Zig-zag case (node and parent are on opposite sides)
            # 3-1. Node is right child of parent, and parent is left child of grandparent
            elif node == parent.right and parent == grand.left:
                # Perform left rotation on parent, then right rotation on grandparent
                self._rotate_left(parent)
                self._rotate_right(grand)

            # 3-2. Node is left child of parent, and parent is right child of grandparent
            elif node == parent.left and parent == grand.right:
                # Perform right rotation on parent, then left rotation on grandparent
                self._rotate_right(parent)
                self._rotate_left(grand)


# need to implement rotate_left and rotate_right methods
    def _rotate_left(self, x):
        y = x.right
        if not y: return
        x.right = y.left
        if y.left: y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        y = x.left
        if not y: return
        x.left = y.right
        if y.right: y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

# modified search method to include splaying
    def search(self, search_node):
        node = self.root
        last = None
        while node:
            last = node
            if search_node == node.key:
                self._splay(node)  # Splay the found node
                return node
            elif search_node < node.key:
                node = node.left
            else:
                node = node.right
        if last:  # Splay the last accessed node even on failed search
            self._splay(last)
        return None

# modified insert method to include splaying
    def insert(self, target):
        if not self.root:
            self.root = BSTNode(target)
            return
        node = self.root
        while True:
            if target < node.key:
                if node.left:
                    node = node.left
                else:
                    node.left = BSTNode(target, node)
                    self._splay(node.left)
                    return
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = BSTNode(target, node)
                    self._splay(node.right)
                    return


# modified delete method to include splaying - at end of deletion

if node.parent:
    self._splay(node.parent)
