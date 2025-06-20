"""
Red-Black Tree Implementation
-----------------------------
A self-balancing binary search tree with the following properties:
1. Every node is either red or black.
2. The root is always black.
3. Red nodes cannot have red children (no two reds in a row).
4. Every path from a node to its descendant NIL nodes contains the same number of black nodes.

Components:
-----------
- `RBNode`: Holds key, color, parent, left/right child.
- `NIL`: Sentinel black node used instead of None.

Key Methods:
------------
- `insert(key)`: Standard BST insert followed by rebalancing using `_fix_insert`.
- `_fix_insert(node)`: Restores Red-Black properties using rotations and recoloring.
- `_rotate_left` / `_rotate_right`: Standard BST rotations with parent updates.
- `search(key)`: Standard BST search.
- `inorder(node)`: In-order traversal printing keys and colors.

Balancing:
----------
- Insertions may temporarily violate Red-Black rules.
- Rebalancing fixes double-red violations using three main cases: 
  1. Recoloring (uncle is red),
  2. Rotation (node is inside or outside grandparent's subtree).
"""


class RBNode:
    def __init__(self, key, color='red', parent=None):
        self.key = key               # Value stored in the node
        self.color = color           # Node color: 'red' or 'black'
        self.left = None             # Left child
        self.right = None            # Right child
        self.parent = parent         # Parent node

class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None, color='black')  # Sentinel NIL node
        self.root = self.NIL                    # Initialize tree as empty

# --------------------------- Search ---------------------------

    def search(self, key, node=None):
        # 1. Start from root if no node is given
        if node is None:
            node = self.root
        # 2. Traverse tree until match or NIL
        while node != self.NIL and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

# --------------------------- Insertion ---------------------------

    def insert(self, key):
        # 1. Create new red node
        new_node = RBNode(key)
        new_node.left = new_node.right = self.NIL

        # 2. Standard BST insertion
        parent = None
        node = self.root
        while node != self.NIL:
            parent = node
            if new_node.key < node.key:
                node = node.left
            else:
                node = node.right

        # 3. Set parent of new node
        new_node.parent = parent
        if not parent:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # 4. Fix Red-Black Tree properties
        self._fix_insert(new_node)

# --------------------------- Insertion Fix ---------------------------

    def _fix_insert(self, node):
        # While parent is red (double red violation)
        while node != self.root and node.parent.color == 'red':
            parent = node.parent
            grand = parent.parent

            # Parent is left child of grandparent
            if parent == grand.left:
                uncle = grand.right

                # Case 1: Uncle is red → recolor
                if uncle.color == 'red':
                    parent.color = 'black'
                    uncle.color = 'black'
                    grand.color = 'red'
                    node = grand  # Continue upward
                else:
                    # Case 2: Node is right child → left rotate
                    if node == parent.right:
                        node = parent
                        self._rotate_left(node)
                    # Case 3: Node is left child → right rotate
                    parent.color = 'black'
                    grand.color = 'red'
                    self._rotate_right(grand)

            # Parent is right child of grandparent (mirror cases)
            else:
                uncle = grand.left
                if uncle.color == 'red':
                    parent.color = 'black'
                    uncle.color = 'black'
                    grand.color = 'red'
                    node = grand
                else:
                    if node == parent.left:
                        node = parent
                        self._rotate_right(node)
                    parent.color = 'black'
                    grand.color = 'red'
                    self._rotate_left(grand)

        # Root must always be black
        self.root.color = 'black'

# --------------------------- Rotation ---------------------------

    def _rotate_left(self, x):
        # 1. Right child becomes new parent of subtree
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent

        # 2. Update parent's reference
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _rotate_right(self, y):
        # 1. Left child becomes new parent of subtree
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent

        # 2. Update parent's reference
        if not y.parent:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

# --------------------------- Utility ---------------------------

    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node != self.NIL:
            self.inorder(node.left)
            print(f"{node.key}({node.color})", end=' ')
            self.inorder(node.right)
