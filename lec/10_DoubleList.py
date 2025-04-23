class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

#------------------------------------------------------------------------------------

# Double linked

class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation"""

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node"""
        def __init__(self, element, prev, next):
            # Initialize a node with an element, a reference to the previous node, and a reference to the next node
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list."""
        # Create header and trailer sentinel nodes
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        # Link header and trailer to each other
        self._header._next = self._trailer
        self._trailer._prev = self._header
        # Initialize size of the list to 0
        self._size = 0

    def __len__(self):
        """Return the number of elements in the list"""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node"""
        # Create a new node with element e, linking it between predecessor and successor
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest  # Update predecessor's next to point to the new node
        successor._prev = newest  # Update successor's prev to point to the new node
        self._size += 1  # Increment the size of the list
        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element"""
        # Get references to the node's predecessor and successor
        predecessor = node._prev
        successor = node._next
        # Bypass the node to be deleted
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1  # Decrement the size of the list
        # Store the element to return and clear the node's references
        element = node._element
        node._prev = node._next = node._element = None
        return element

#------------------------------------------------------------------------------------

# Double ended queue

class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque.
        
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():  # Check if the deque is empty
            raise Empty("Deque is empty")  # Raise an exception if empty
        return self._header._next._element  # Return the element of the first node (just after the header)

    def last(self):
        """Return (but do not remove) the element at the back of the deque.
        
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():  # Check if the deque is empty
            raise Empty("Deque is empty")  # Raise an exception if empty
        return self._trailer._prev._element  # Return the element of the last node (just before the trailer)

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        # Insert a new node with element e between the header and the current first node
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Add an element to the back of the deque."""
        # Insert a new node with element e between the current last node and the trailer
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Remove and return the element from the front of the deque.
        
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():  # Check if the deque is empty
            raise Empty("Deque is empty")  # Raise an exception if empty
        # Remove the first node (just after the header) and return its element
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the back of the deque.
        
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():  # Check if the deque is empty
            raise Empty("Deque is empty")  # Raise an exception if empty
        # Remove the last node (just before the trailer) and return its element
        return self._delete_node(self._trailer._prev)


#------------------------------------------------------------------------------------

# Positional List
# A positional list is a type of linked list.
# Instead of using index numbers, we use "positions" to refer to elements.
# Each position points to one element in the list.
# You can insert, delete, or replace elements using these positions.
# This makes it easier and safer to work with the list, especially in the middle.


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    #-------------------------- nested Position class --------------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container  # Reference to the list containing this position
            self._node = node  # Reference to the node at this position

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element  # Access the element stored in the node

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            # Check if the other object is the same type and references the same node
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)  # Opposite of __eq__

    #-------------------------- utility methods --------------------------
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):  # Ensure p is a Position instance
            raise TypeError("p must be proper Position type")
        if p._container is not self:  # Ensure p belongs to this container
            raise ValueError("p does not belong to this container")
        if p._node._next is None:  # Check if the node is deprecated
            raise ValueError("p is no longer valid")
        return p._node  # Return the node associated with the position

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:  # Check if node is a sentinel
            return None  # Return None for boundary violations
        else:
            return self.Position(self, node)  # Create a Position for the node

    #-------------------------- accessors --------------------------
    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)  # Position of the first element

    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)  # Position of the last element

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)  # Validate the position
        return self._make_position(node._prev)  # Position of the previous node

    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)  # Validate the position
        return self._make_position(node._next)  # Position of the next node

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()  # Start at the first position
        while cursor is not None:  # Continue until the end of the list
            yield cursor.element()  # Yield the element at the current position
            cursor = self.after(cursor)  # Move to the next position

    #-------------------------- mutators --------------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)  # Insert the node
        return self._make_position(node)  # Return the position of the new node

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)  # Insert at the front

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)  # Insert at the back

    def add_before(self, p, e):
        """Insert element e into the list before Position p and return new Position."""
        original = self._validate(p)  # Validate the position
        return self._insert_between(e, original._prev, original)  # Insert before the position

    def add_after(self, p, e):
        """Insert element e into the list after Position p and return new Position."""
        original = self._validate(p)  # Validate the position
        return self._insert_between(e, original, original._next)  # Insert after the position

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)  # Validate the position
        return self._delete_node(original)  # Remove the node and return its element

    def replace(self, p, e):
        """Replace the element at Position p with e.
        
        Return the element formerly at Position p.
        """
        original = self._validate(p)  # Validate the position
        old_value = original._element  # Store the old element
        original._element = e  # Replace with the new element
        return old_value  # Return the old element
