class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

#------------------------------------------------------------------------------------

# Node class for list nodes

""" java
public class Node {
    // Instance variables:
    private Object element;
    private Node next;

    /** Creates a node with null references to its element and next node. */
    public Node() {
        this(null, null);
    }

    /** Creates a node with the given element and next node. */
    public Node(Object e, Node n) {
        element = e;
        next = n;
    }

    // Accessor methods:
    public Object getElement() {
        return element;
    }

    public Node getNext() {
        return next;
    }

    // Modifier methods:
    public void setElement(Object newElem) {
        element = newElem;
    }

    public void setNext(Node newNext) {
        next = newNext;
    }
}
"""

class Node:
    # Constructor to initialize a node with an element and a reference to the next node
    def __init__(self, element=None, next=None):
        self._element = element  # The data stored in the node
        self._next = next        # Reference to the next node in the list

    # Method to get the element stored in the node
    def get_element(self):
        return self._element

    # Method to get the reference to the next node
    def get_next(self):
        return self._next

    # Method to update the element stored in the node
    def set_element(self, new_elem):
        self._element = new_elem

    # Method to update the reference to the next node
    def set_next(self, new_next):
        self._next = new_next

#------------------------------------------------------------------------------------

# Stack as a Linked List

class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    #-------------------- nested _Node class ---------------------------------------

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node"""
        __slots__ = '_element', '_next'  # Use __slots__ to save memory

        def __init__(self, element, next):
            self._element = element  # The data stored in the node
            self._next = next        # Reference to the next node in the stack

    #-------------------- stack methods ---------------------------------------
    def __init__(self):
        """Create an empty stack"""
        self._head = None  # Reference to the head (top) of the stack
        self._size = 0     # Number of elements in the stack

    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        # Create a new node with the element and set it as the new head
        self._head = self._Node(e, self._head)
        self._size += 1  # Increment the size of the stack

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty('Stack is empty')  # Raise exception if stack is empty
        return self._head._element  # Return the element at the top of the stack

    def pop(self):
        """Remove and return the element from the top of the stack (i.e LIFO).
        
        Raise Empty exception if the stack is empty"""
        if self.is_empty():
            raise Empty('Stack is empty')  # Raise exception if stack is empty
        answer = self._head._element  # Get the element at the top of the stack
        self._head = self._head._next  # Update the head to the next node
        self._size -= 1  # Decrement the size of the stack
        return answer  # Return the removed element
    

#------------------------------------------------------------------------------------

# Queue as a Linked List

class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage"""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node"""
        __slots__ = '_element', '_next'  # Use __slots__ to save memory by limiting instance attributes

        def __init__(self, element, next):
            self._element = element  # The data stored in the node
            self._next = next        # Reference to the next node in the queue

    def __init__(self):
        """Create an empty queue"""
        self._head = None  # Reference to the head (front) of the queue
        self._tail = None  # Reference to the tail (end) of the queue
        self._size = 0     # Number of elements in the queue

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty')  # Raise exception if the queue is empty
        return self._head._element  # Return the element at the front of the queue

    def dequeue(self):
        """Remove and return the first element of the queue (i.e. FIFO).
        
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty')  # Raise exception if the queue is empty

        answer = self._head._element  # Get the element at the front of the queue
        self._head = self._head._next  # Update the head to the next node
        self._size -= 1  # Decrement the size of the queue
        if self.is_empty():  # If the queue is now empty
            self._tail = None  # Set the tail to None as well
        return answer  # Return the removed element

    def enqueue(self, e):
        """Add an element to the back of the queue."""
        newest = self._Node(e, None)  # Create a new node with the element and no next node
        if self.is_empty():  # If the queue is empty
            self._head = newest  # Set the new node as the head
        else:
            self._tail._next = newest  # Link the current tail to the new node
        self._tail = newest  # Update the tail to the new node
        self._size += 1  # Increment the size of the queue