class TreeNode:
    """Class representing a node in a tree."""
    def __init__(self, value):
        self.value = value            # Value stored in the node
        self.children = []            # List of child nodes

    def add_child(self, child_node):
        """Add a child node to this node."""
        self.children.append(child_node)

    def __repr__(self, level=0):
        """String representation of the tree rooted at this node (indented)."""
        ret = "  " * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


class Tree:
    """Class representing a tree."""
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def __repr__(self):
        return repr(self.root)



#----------------------------------------------

class BinaryTreeNode:
    """A node in a binary tree."""
    def __init__(self, value):
        self.value = value          # The value stored in the node
        self.left = None            # Left child
        self.right = None           # Right child

    def insert_left(self, value):
        """Insert a new node as the left child."""
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        """Insert a new node as the right child."""
        self.right = BinaryTreeNode(value)
        return self.right

    def __repr__(self, level=0):
        """String representation of the binary tree."""
        ret = "  " * level + repr(self.value) + "\n"
        if self.left:
            ret += self.left.__repr__(level + 1)
        if self.right:
            ret += self.right.__repr__(level + 1)
        return ret

#----------------------------------------------

class LinkedBinaryTree:
    """Linked representation of a binary tree structure."""

    class _Node:
        """Lightweight, non-public class for storing a node."""
        def __init__(self, element, parent=None, left=None, right=None):
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._root

    def add_root(self, e):
        """Place element e at the root of an empty tree and return the node."""
        if self._root is not None:
            raise ValueError("Root exists")
        self._root = self._Node(e)
        self._size = 1
        return self._root

    def add_left(self, node, e):
        """Create a new left child for node storing element e."""
        if node.left is not None:
            raise ValueError("Left child exists")
        node.left = self._Node(e, parent=node)
        self._size += 1
        return node.left

    def add_right(self, node, e):
        """Create a new right child for node storing element e."""
        if node.right is not None:
            raise ValueError("Right child exists")
        node.right = self._Node(e, parent=node)
        self._size += 1
        return node.right

    def parent(self, node):
        return node.parent

    def children(self, node):
        """Yield children of node."""
        if node.left:
            yield node.left
        if node.right:
            yield node.right

    def __repr__(self):
        """Return a simple text-based tree representation (pre-order)."""
        lines = []
        def _preorder(node, depth=0):
            if node:
                lines.append("  " * depth + repr(node.element))
                _preorder(node.left, depth + 1)
                _preorder(node.right, depth + 1)
        _preorder(self._root)
        return "\n".join(lines)
