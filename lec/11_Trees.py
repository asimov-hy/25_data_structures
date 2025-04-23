class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

#------------------------------------------------------------------------------------

# Tree

class Tree:
    """Abstract base class representing a tree structure."""

    # ------------------- nested Position class -------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')  # Subclasses must define how to return the element

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')  # Subclasses must define equality comparison

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)  # Opposite of __eq__, checks inequality

    # ------------------- abstract methods that concrete subclasses must support -------------------

    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')  # Subclasses must define how to get the root

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError('must be implemented by subclass')  # Subclasses must define how to get the parent of a position

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')  # Subclasses must define how to count children of a position

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('must be implemented by subclass')  # Subclasses must define how to iterate over children

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')  # Subclasses must define how to calculate the size of the tree

    # ------------------- concrete methods implemented in this class -------------------

    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p  # Checks if the given position is the root

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0  # Checks if the position has no children

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0  # Checks if the tree has no elements


    #-------------------------- extra ----------------

    def depth(self, p):
        """
        Return the number of levels separating Position p from the root.
        Depth of root is 0. Depth of any other node is 1 + depth of its parent.
        This is a recursive implementation.
        """
        if self.is_root(p):  # Check if the position p is the root of the tree
            return 0  # The depth of the root is 0
        else:
            # Recursively calculate the depth by adding 1 to the depth of the parent of p
            return 1 + self.depth(self.parent(p))  # Move up one level and calculate depth
        
    def _height1(self): # defined but not used
        """
        Return the height of the tree.
        This method checks the depth of every leaf and returns the max.
        It works, but it's inefficient: O(n^2) in the worst case (many recursive depth calls).
        """
        # Generate the depth of each leaf node and return the maximum value
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """
        Return the height of the subtree rooted at Position p.
        This is more efficient — runs in O(n) time relative to size of subtree.
        Recursively computes the height: 1 + max height of children.
        """
        if self.is_leaf(p):  # Base case: if the position is a leaf, its height is 0
            return 0
        else:
            # Recursively calculate the height as 1 + maximum height of all children
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """
        Return the height of the subtree rooted at Position p.
        If p is None, return the height of the entire tree.
        """
        if p is None:  # If no position is provided, calculate the height of the entire tree
            p = self.root()  # Start from the root of the tree
        # Use the efficient _height2 method to calculate the height
        return self._height2(p)

#------------------------------------------------------------------------------------

# Binary Tree

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure.
    Extends the Tree class with left, right, and sibling access.
    """

    # --------------------- abstract methods ---------------------

    def left(self, p):
        """Return a Position representing p's left child (or None if no left child)."""
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """Return a Position representing p's right child (or None if no right child)."""
        raise NotImplementedError('must be implemented by subclass')

    # --------------------- concrete methods ---------------------

    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:
            return None  # p is the root; root has no sibling
        if p == self.left(parent):
            return self.right(parent)  # may be None
        else:
            return self.left(parent)  # may be None

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

#------------------------------------------------------------------------------------

# Linked Binary Tree

class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    # --------------------- nested _Node class ---------------------
    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_left', '_right'  # Use slots to save memory

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element  # Store the element
            self._parent = parent  # Reference to the parent node
            self._left = left  # Reference to the left child
            self._right = right  # Reference to the right child

    # --------------------- Position abstraction ---------------------
    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""
        def __init__(self, container, node):
            self._container = container  # Reference to the tree container
            self._node = node  # Reference to the node

        def element(self):
            return self._node._element  # Return the element stored in the node

    # --------------------- utility methods ---------------------
    def _validate(self, p):
        """Return node if position is valid, else raise error."""
        if not isinstance(p, self.Position):  # Check if p is a valid Position
            raise TypeError('p must be a proper Position type')
        if p._container is not self:  # Ensure p belongs to this tree
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:  # Check if node is deprecated
            raise ValueError('p is no longer valid')
        return p._node  # Return the node associated with the position

    def _make_position(self, node):
        """Return Position instance for a node (or None if node is None)."""
        return self.Position(self, node) if node is not None else None  # Create a Position or return None

    # --------------------- binary tree constructor ---------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None  # Initialize the root as None
        self._size = 0  # Initialize the size of the tree as 0

    # --------------------- public accessors ---------------------
    def __len__(self):
        return self._size  # Return the number of elements in the tree

    def root(self):
        return self._make_position(self._root)  # Return the root position

    def parent(self, p):
        node = self._validate(p)  # Validate the position
        return self._make_position(node._parent)  # Return the parent position

    def left(self, p):
        node = self._validate(p)  # Validate the position
        return self._make_position(node._left)  # Return the left child position

    def right(self, p):
        node = self._validate(p)  # Validate the position
        return self._make_position(node._right)  # Return the right child position

    # --------------------- nonpublic mutators ---------------------
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return Position."""
        if self._root is not None:  # Check if the root already exists
            raise ValueError('Root exists')
        self._size = 1  # Update the size of the tree
        self._root = self._Node(e)  # Create a new root node
        return self._make_position(self._root)  # Return the root position

    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e."""
        node = self._validate(p)  # Validate the position
        if node._left is not None:  # Check if the left child already exists
            raise ValueError('Left child exists')
        self._size += 1  # Increment the size of the tree
        node._left = self._Node(e, node)  # Create a new left child node
        return self._make_position(node._left)  # Return the left child position

    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e."""
        node = self._validate(p)  # Validate the position
        if node._right is not None:  # Check if the right child already exists
            raise ValueError('Right child exists')
        self._size += 1  # Increment the size of the tree
        node._right = self._Node(e, node)  # Create a new right child node
        return self._make_position(node._right)  # Return the right child position

    def _replace(self, p, e):
        """Replace the element at Position p with e and return old element."""
        node = self._validate(p)  # Validate the position
        old = node._element  # Store the old element
        node._element = e  # Replace the element with the new one
        return old  # Return the old element

    def _delete(self, p):
        """Delete node at Position p and replace it with its child, if any."""
        node = self._validate(p)  # Validate the position
        if self.num_children(p) == 2:  # Check if the node has two children
            raise ValueError('Position has two children')

        child = node._left if node._left else node._right  # Get the single child (if any)
        if child is not None:
            child._parent = node._parent  # Update the child's parent reference

        if node is self._root:  # Check if the node is the root
            self._root = child  # Update the root to the child
        else:
            parent = node._parent  # Get the parent node
            if node is parent._left:  # Check if the node is the left child
                parent._left = child  # Update the parent's left reference
            else:
                parent._right = child  # Update the parent's right reference

        self._size -= 1  # Decrement the size of the tree
        node._parent = node  # Mark the node as deprecated
        return node._element  # Return the element of the deleted node


#------------------------------------------------------------------------------------

# Traversal (within tree or binary tree or linked binary tree)

# preorder traversal: mid -> left -> right

    def preorder(self, p):
        """Generate a preorder iteration of positions in the tree."""
        yield p  # Visit the current position
        for c in self.children(p):  # Iterate through the children of the current position
            yield from self.preorder(c)  # Recursively yield positions in preorder

    # postorder traversal: left -> right -> mid

    def postorder(self, p):
        """Generate a postorder iteration of positions in the tree."""
        for c in self.children(p):  # Iterate through the children of the current position
            yield from self.postorder(c)  # Recursively yield positions in postorder
        yield p  # Visit the current position

    # inorder traversal: left -> mid -> right

    def inorder(self, p):
        """Generate an inorder iteration of positions in a binary tree."""
        if self.left(p) is not None:  # Check if the current position has a left child
            yield from self.inorder(self.left(p))  # Recursively yield positions in inorder from the left child
        yield p  # Visit the current position
        if self.right(p) is not None:  # Check if the current position has a right child
            yield from self.inorder(self.right(p))  # Recursively yield positions in inorder from the right child

    # breadth first tree (BFS): by depth starting from top

    from collections import deque  # Import deque for efficient queue operations

    def breadthfirst(self):
        """Generate a breadth-first iteration of positions in the tree."""
        if not self.is_empty():  # Check if the tree is not empty
            fringe = deque()  # Create a deque to use as a queue
            fringe.append(self.root())  # Add the root position to the queue
            while fringe:  # Continue until the queue is empty
                p = fringe.popleft()  # Remove and return the leftmost position from the queue
                yield p  # Visit the current position
                for c in self.children(p):  # Iterate through the children of the current position
                    fringe.append(c)  # Add each child to the queue

    # depth first search (DFS): start by depth

    def depthfirst(self):
        """Generate a depth-first iteration of positions in the tree."""
        if not self.is_empty():  # Check if the tree is not empty
            fringe = deque()  # Create a deque to use as a stack
            fringe.append(self.root())  # Add the root position to the stack
            while fringe:  # Continue until the stack is empty
                p = fringe.pop()  # Remove and return the rightmost position from the stack
                yield p  # Visit the current position
                for c in self.children(p):  # Iterate through the children of the current position
                    fringe.append(c)  # Add each child to the stack

    #---------------------------------------------------------------------------------

    # print arithmetic: print the expression in a parenthesized form
    # for example: 1 + (2 * 3) = (1 + (2 * 3))

    def print_expression(self, p):
        """Print parenthesized infix expression rooted at p."""
        if self.left(p) is not None:  # Check if the current position has a left child
            print("(", end="")  # Print an opening parenthesis
            self.print_expression(self.left(p))  # Recursively print the left subtree
        print(p.element(), end="")  # Print the operator or operand at the current position
        if self.right(p) is not None:  # Check if the current position has a right child
            self.print_expression(self.right(p))  # Recursively print the right subtree
            print(")", end="")  # Print a closing parenthesis

    # evaluate arithmetic: evaluate the expression in a parenthesized form
    # for example: 1 + (2 * 3) = 1 + (2 * 3) = 7
    # the eval function is used to evaluate the expression

    def eval_expr(self, p):
        """Evaluate the arithmetic expression rooted at p."""
        if self.is_leaf(p):  # Check if the current position is a leaf
            return p.element()  # Return the element at the leaf (operand)
        else:
            x = self.eval_expr(self.left(p))  # Recursively evaluate the left subtree
            y = self.eval_expr(self.right(p))  # Recursively evaluate the right subtree
            op = p.element()  # Get the operator at the current position
            return eval(f"{x} {op} {y}")  # Evaluate the expression using the operator and operands

#------------------------------------------------------------------------------------
# Euler Tour Traversal: visits each node three times—before its children, between children, and after its children—during a complete walk around the tree.

class EulerTour:
    """Abstract base class for performing Euler tour of a tree.

    _hook_previsit and _hook_postvisit may be overridden by subclasses
    to customize behavior at specific points of the traversal.
    """

    def __init__(self, tree):
        """Prepare an Euler tour template for given tree."""
        self._tree = tree  # The tree to traverse

    def tree(self):
        """Return reference to the tree being traversed."""
        return self._tree  # Return the tree object

    def execute(self):
        """
        Perform the tour and return any result from post visit of root.
        Starts the recursion from the root of the tree.
        """
        if len(self._tree) > 0:  # Check if the tree is not empty
            return self._tour(self._tree.root(), 0, [])  # Start the tour from the root, depth 0, and an empty path

    def _tour(self, p, d, path):
        """
        Perform Euler tour of subtree rooted at Position p.

        p     -- Position of current node being visited
        d     -- depth of p in the tree
        path  -- list of indices of children on path from root to p
        """
        self._hook_previsit(p, d, path)  # Customizable hook before visiting children
        results = []  # List to store results from children

        path.append(0)  # Add new index to end of path before recursion
        for c in self._tree.children(p):  # Recursively tour subtrees
            result = self._tour(c, d + 1, path)  # Perform tour on child
            results.append(result)  # Collect result from child
            path[-1] += 1  # Increment index for the next child
        path.pop()  # Remove extraneous index from end of path

        answer = self._hook_postvisit(p, d, path, results)  # Customizable hook after visiting children
        return answer  # Return the result of the post-visit

    def _hook_previsit(self, p, d, path):
        """Visit Position p, before the tour of its children."""
        pass  # To be overridden by subclasses

    def _hook_postvisit(self, p, d, path, results):
        """Visit Position p, after the tour of its children.

        p       -- current node
        d       -- depth of p in the tree
        path    -- list of indices of children from root to p
        results -- list of results returned from _hook_postvisit(c) for each child c of p
        """
        pass  # To be overridden by subclasses

#------------------------------------------------------------------------------------
# Parenthesize Tour: an Euler Tour variant that prints the tree structure as a fully parenthesized expression.

class ParenthesizeTour(EulerTour):
    """Print parenthesized representation of tree."""

    def _hook_previsit(self, p, d, path):
        """Pre-visit: print element and opening '(' if p has children"""
        if path and path[-1] > 0:  # If not the first child
            print(", ", end="")  # Add comma separator
        print(p.element(), end="")  # Print the element
        if not self._tree.is_leaf(p):  # If the position has children
            print(" (", end="")  # Print an opening parenthesis

    def _hook_postvisit(self, p, d, path, results):
        """Post-visit: print closing ')' if p has children"""
        if not self._tree.is_leaf(p):  # If the position has children
            print(")", end="")  # Print a closing parenthesis

#------------------------------------------------------------------------------------
# Disk Space Tour: an Euler Tour variant that computes the disk space of each subtree.

class DiskSpaceTour(EulerTour):
    """Compute disk space of each subtree rooted at p."""

    def _hook_postvisit(self, p, d, path, results):
        """
        Sum the disk space of all children and add p's own space.

        p.element().space() returns space used by this node
        sum(results) is total from children
        """
        return p.element().space() + sum(results)  # Add the space of the current node to the total space of its children
