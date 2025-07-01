from a1 import BinarySearchTree

# 1. Define a function to find the minimum key in the BST.
def min_tree(self):
    # 2. Start from the root of the tree.
    node = self.root

    # 3. If the tree is empty, return None.
    if node is None:
        return None

    # 4. Traverse to the leftmost node (the minimum).
    while node.left:
        node = node.left

    # 5. Return the key of the leftmost node.
    return node.key


# 6. Define a function to find the maximum key in the BST.
def max_tree(self):
    # 7. Start from the root of the tree.
    node = self.root

    # 8. If the tree is empty, return None.
    if node is None:
        return None

    # 9. Traverse to the rightmost node (the maximum).
    while node.right:
        node = node.right

    # 10. Return the key of the rightmost node.
    return node.key
