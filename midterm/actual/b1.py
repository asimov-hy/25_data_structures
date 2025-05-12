## Problem b1: Preorder Traversal

# (Easy, 5 points)

# Implement the following function:
# - `preorder(tree: BinaryTree) -> list<int>`: This function takes a binary tree `tree` as input and 
#       returns a list of `key`s of the nodes in the tree, starting from the root, traversed in a *preorder* manner.
#     A preorder traversal visits the nodes in the following order: parent, left child, right child.
#     For example, a binary tree with the following structure:

#     ```plaintext
#             1
#           /    \
#          9      8
#         / \    / 
#        6   2  3
#     ```

#     Should output a python list: `[1, 9, 6, 2, 8, 3]`.
#     Note: Use a recursive approach to implement the postorder traversal.
#     Note2: Return an empty list if the tree is empty.
#     Note3: You can get the root node of the tree by calling `tree.root()`.

# todo: implement this
def preorder(tree):
    traversal = []
    def _preorder(node):
        if node is None:
            return
        traversal.append(node.key)
        _preorder(node.left)
        _preorder(node.right)
    _preorder(tree.root())
    return traversal

