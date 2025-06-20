"""
Splay Tree Implementation (based on Binary Search Tree)
--------------------------------------------------------

This extension of a BST includes splaying: a self-adjusting mechanism to improve access time for recently used nodes.

Splaying Logic:
- After `search`, `insert`, or `delete`, the accessed node (or its parent) is rotated up to the root.
- Uses three cases:
  1. Zig: One rotation if node's parent is root.
  2. Zig-zig: Two same-side rotations (left-left or right-right).
  3. Zig-zag: Two opposite-side rotations (left-right or right-left).

Modified Methods:
- `search(key)`: Performs normal BST search, then splays the found or last visited node.
- `insert(key)`: Standard BST insert followed by splaying the inserted node.
- `delete(key)`: After deletion, splays the deleted node's parent if it exists.

Rotations:
- `_rotate_left(x)`: Promotes right child `y` of `x`.
- `_rotate_right(x)`: Promotes left child `y` of `x`.

Purpose:
- Keeps recently accessed nodes near the top to optimize future lookups.
- Maintains BST structure while offering amortized O(log n) performance.
"""

def _splay(self, node):
    while node.parent:
        parent = node.parent
        grand = parent.parent

        if not grand:
            # Zig
            if node == parent.left:
                self._rotate_right(parent)
            else:
                self._rotate_left(parent)
        elif node == parent.left and parent == grand.left:
            # Zig-Zig (left-left)
            self._rotate_right(grand)
            self._rotate_right(parent)
        elif node == parent.right and parent == grand.right:
            # Zig-Zig (right-right)
            self._rotate_left(grand)
            self._rotate_left(parent)
        elif node == parent.right and parent == grand.left:
            # Zig-Zag (left-right)
            self._rotate_left(parent)
            self._rotate_right(grand)
        elif node == parent.left and parent == grand.right:
            # Zig-Zag (right-left)
            self._rotate_right(parent)
            self._rotate_left(grand)

# --------------------------- rorate helpers ---------------------------

def _rotate_left(self, x):
    y = x.right
    if not y: return
    x.right = y.left
    if y.left:
        y.left.parent = x
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
    if y.right:
        y.right.parent = x
    y.parent = x.parent
    if not x.parent:
        self.root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y

# ---------------------------








    def search(self, search_node):
        node = self.root
        last = None
        while node:
            last = node
            if search_node == node.key:
                self._splay(node)
                return node
            elif search_node < node.key:
                node = node.left
            else:
                node = node.right
        if last:
            self._splay(last)  # Splay nearest accessed node
        return None

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

# add end of delete
        if node.parent:
            self._splay(node.parent)
