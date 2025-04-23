class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self.__data = []                 # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)
    
    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0
    
    def push(self, e):
        """Add element e to the top of the stack"""
        self._data.append(e)            # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty.
        """

        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]           # the last item in the list
    
    def pop(self):
        """Remove and return the element from the top of the stack (i.e. LIFO).
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()         # remove last item from list
    
#----------------------------------------------------------------------------------------------

# Parentheses Matching Algorithm

def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise."""
    lefty = '({['       # opening delimeters
    righty = ')}]'      # respective closing delims
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)           # push left delimter on stack

        elif c in righty:
            if S.is_empty():
                return False    # nothing to match with
            
            if righty.index(c) != lefty.index(S.pop()):
                return False    # mismatched
    return S.is_empty()         # were all symbols matched?

#----------------------------------------------------------------------------------------------

# Tag Matching Algorithm

def is_matched_html(raw):
    """Return True if all HTML tags are properly match; False otherwise"""
    S = ArrayStack()
    j = raw.find('<')           # find first '<' character (if any)
    while j != -1:
        k = raw.find('>', j+1)  # find next '>' character

        if k == -1:
            return False        # invalid tag
        
        tag = raw[j+1:k]        # strip away <>
        if not tag.starswith('/'):  # this is opening tag
            S.push(tag)
        else:                   # this is closing tag
            if S.is_empty():
                return False        # nothing to match with
            if tag[1:] != S.pop():
                return False        # mismatched delimiter
        j = raw.find('<', k+1)      # find next '<' character (if any)

    return S.is_empty       # were all opening tags matched?

#----------------------------------------------------------------------------------------------

# Evaluating Expression

def eval_exp(tokens):
    """Evaluate an arithmetic expression using textbook two-stack algorithm."""
    opStk = ArrayStack()        # holds operators
    valStk = ArrayStack()       # holds values

    def prec(op):
        """Operator precedence: $ < + - < * /"""
        if op == '$':       # special 'end of input' token with lowest precedence
            return 0
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return -1

    def do_op():
        x = valStk.pop()
        y = valStk.pop()
        op = opStk.pop()
        if op == '+':
            valStk.push(y + x)
        elif op == '-':
            valStk.push(y - x)
        elif op == '*':
            valStk.push(y * x)
        elif op == '/':
            valStk.push(y / x)

    def repeat_ops(ref_op):
        while len(opStk) > 0 and prec(ref_op) <= prec(opStk.top()):
            do_op()

    tokens.append('$')  # Add end-of-input marker

    for z in tokens:
        if isinstance(z, (int, float)):  # isNumber(z)
            valStk.push(z)
        else:  # it's an operator
            repeat_ops(z)
            opStk.push(z)

    repeat_ops('$')  # Final flush of remaining ops
    return valStk.top()

#----------------------------------------------------------------------------------------------

# span
# The span S[i] of X[i] is the number of consecutive elements ending at X[i] that are less than or equal to X[i].

# Quadratic Span

def spans1(X):
    """Compute spans using the naive O(n^2) algorithm."""
    n = len(X)
    S = [0] * n  # Output list to store spans for each element

    for i in range(n):
        s = 1  # Start with a span of 1 (the element itself)
        # Go backwards and count how many consecutive elements
        # before X[i] are less than or equal to X[i]
        while s <= i and X[i - s] <= X[i]:
            s += 1
        S[i] = s  # Store the computed span

    return S

# Linear Span

class ArrayStack:
    """A simple stack implementation using Python list."""
    def __init__(self):
        self._data = []

    def push(self, e):
        self._data.append(e)  # Add item to the top of the stack

    def pop(self):
        return self._data.pop()  # Remove and return the top item

    def top(self):
        return self._data[-1]  # Peek at the top item without removing

    def is_empty(self):
        return len(self._data) == 0


def spans2(X):
    """Compute spans using a stack in O(n) time."""
    n = len(X)
    S = [0] * n           # Output array for spans
    A = ArrayStack()      # Stack to hold indices of elements

    for i in range(n):
        # Pop indices from the stack while their values are less than or equal to X[i]
        while not A.is_empty() and X[A.top()] <= X[i]:
            A.pop()

        # If the stack is empty, it means all previous elements were smaller
        if A.is_empty():
            S[i] = i + 1   # Span is entire range from 0 to i (inclusive)
        else:
            S[i] = i - A.top()  # Span is distance to the last larger element

        A.push(i)  # Push current index onto the stack for future comparisons

    return S
