# Problem b: Binary Trees

(34 points)

In this problem, you are tasked with developing a series of functions for binary trees where each node contains a unique `key`. A base structure for the `BinaryTree` class is provided for you.

A `_Node` class is also provided, which represents a single node within the binary tree. Each node stores a `key`, a reference to its `parent`, as well as references to its `left` and `right` children.

You can assume that the binary tree is *complete*, meaning that each level of the tree is fully filled, except possibly for the last level, which is filled from *left to right*.

## Problem b1: Preorder Traversal

(Easy, 5 points)

Implement the following function:

- `preorder(tree: BinaryTree) -> list<int>`: This function takes a binary tree `tree` as input and returns a list of `key`s of the nodes in the tree, starting from the root, traversed in a *preorder* manner.

    A preorder traversal visits the nodes in the following order: parent, left child, right child.

    For example, a binary tree with the following structure:

    ```plaintext
            1
          /    \
         9      8
        / \    / 
       6   2  3
    ```

    Should output a python list: `[1, 9, 6, 2, 8, 3]`.

    Note: Use a recursive approach to implement the postorder traversal.

    Note2: Return an empty list if the tree is empty.

    Note3: You can get the root node of the tree by calling `tree.root()`.

## Problem b2: Postorder Traversal

(Easy, 5 points)

Implement this function:

- `postorder(tree: BinaryTree) -> list<int>`: This function takes a binary tree `tree` as input and returns a list of `key`s of the nodes in the tree, starting from the root, traversed in a *postorder* manner.

    A postorder traversal visits the nodes in the following order: left child, right child, parent.

    For example, a binary tree with the following structure:

    ```plaintext
            1
          /    \
         9      8
        / \    / 
       6   2  3
    ```

    Should output a python list: `[6, 2, 9, 3, 8, 1]`.

## Problem b3: Depth of a Node

(Medium, 8 points)

Implement this function:

- `depth(tree: BinaryTree, key: int) -> int`: This function receives a binary tree `tree` and an integer `key`, and returns the depth of the corresponding node. If the specified `key` does not exist within the tree, the function should return `-1`.

    For example, in the tree below:

    ```plaintext
            1
          /    \
         9      8
        / \    / 
       6   2  3
    ```

    The depth of the node with key `1` is `0` (the root node), the depth of the node with key `3` is `2`, and the depth of the node with key `9` is `1`.

## Problem b4: Find Uncle

(Medium, 8 points)

Implement this function:

- `uncle(tree: BinaryTree, key: int) -> int`: This function takes a binary tree `tree` and an integer `key`, and returns the `key` of the "uncle" node of the specified node. If the specified node does not have an uncle, return `-1`. If the specified node does not exist in the tree, return `-1`.

    The uncle of a node is defined as the sibling of its parent. If the parent node has no sibling, or if the specified node is the root, return `-1`.

    For example, in the tree below:

    ```plaintext
            1
          /    \
         9      8
        / \    / 
       6   2  3
    ```

    The uncle of the node with key `6` is `8`, and the uncle of the node with key `3` is `9`. The uncle of the root node (key `1`) is `-1`, since it has no parent. The uncle of the node with key `9` is also `-1`, since its parent (key `1`) has no sibling.

## Problem b5: Maximum Path Sum

(Medium, 8 points)

Implement this function:

- `max_path_sum(tree: BinaryTree) -> int`: This function takes a binary tree `tree` as input and returns the maximum path sum in the tree.

    The path sum is defined as the sum of the `key`s of all nodes along a path from the root node to any leaf node.

    For example, in the tree below:

    ```plaintext
            1
          /    \
         9      8
        / \    / 
       6   2  3
    ```

    The maximum path sum is when traversing the path `1 -> 9 -> 6`, which equals `1 + 9 + 6 = 16`.

    Note: When the tree is empty, return `0`.

    Note2: When the tree has only a root node, the maximum path sum is equal to the `key` of the root node.
