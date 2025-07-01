# Problem a: Binary Search Tree

A binary search tree (BST) is a binary tree where each node has a key and a value. The key of the left child is less than the key of the parent node, and the key of the right child is greater than the key of the parent node.

The following is an example of a binary search tree:

```plaintext
         (5, 1)
        /      \
    (3, 9)      (7, 8)
    /    \      / 
(1, 6)(4, 2) (6, 1)
```

The base structure for the `TreeMapSkeleton` class is provided for you.

## Problem a1: Searching for a Key

(Medium, 8 points)

Finish implementing the `TreeMapBase1` class. Currently, the `_subtree_search` method is not fully implemented. Implement this method to complete the `TreeMapBase1` class.

- `_subtree_search(self, node: Node, key: int) -> Node`: This function takes a `node` and a `key` to find as input and returns the `node` with the specified `key` if it exists within the subtree rooted at the given `node`.

    If the specified `key` does not exist within the subtree, the function should return the node where the search ended (i.e., the node where the key should be inserted).

    For example, in the tree above, `_subtree_search(self.root, 4)` should return the node with key 4, while `_subtree_search(self.root, 2)` is unable to find the key 2 and should return the node with key 1.

## Problem a2: Inserting or Updating a Node

(Medium, 8 points)

Implement the following function in the `TreeMapBase2` class:

- `__setitem__(self, key: int, value: Any)`: This function takes a `key` and a `value` to insert or update as input and inserts a new node with the specified `key` and `value` into the binary search tree. If a node with the specified `key` already exists, the function should update the `value` of the existing node.

    For example, in the tree above, `__setitem__(4, 9)` should update the value of the node with key 4 to 9, while `__setitem__(8, 3)` should insert a new node with key 8 and value 3.

    Note: You should first search for the key using the `_subtree_search` function. If the key exists, update the value; otherwise, insert a new node.

    Note 2: You can create a new node using the `Node` class provided for you: `self.Node(key: int, value: Any, parent: Node | None)`

## Problem a3: Finding the Node with the Minimum Key

(Easy, 5 points)

Implement the following function:

- `_subtree_first_node(node: Node) -> Node`: This function takes a `node` as input and returns the node with 
- the minimum key within the subtree rooted at the given `node`.

    For example, `_subtree_first_node(self.root)` should return the node with key 1.

# Problem a4: What's next?

(Hard, 10 points)

Implement the following function:

- `after(node: Node) -> Node`: This function takes a `node` as input and returns the next node in the in-order traversal of the binary search tree. If the given `node` is the last node in the traversal, the function should return `None`.

    For example, `after(self.root)` should return the node with key 6, while `after(self.root.left)` should return the node with key 4, and `after(self.root.right)` should return `None`.

    Hint: Here are the rules for finding the next node in the in-order traversal:

    1. If the given node has a right child, the next node in the in-order traversal is the leftmost node of the right subtree.

    2. Otherwise, you should traverse the parent nodes until you find a node that is the left child of its parent. This parent will be the next node in the in-order traversal.

        - Note that the parent of the root node is `None`, so you should stop traversing when you reach the root node.
