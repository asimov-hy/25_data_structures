## Problem b2: Postorder Traversal

# Implement this function:

# - `postorder(tree: BinaryTree) -> list<int>`: This function takes a binary tree `tree` as input and returns a list of `key`s of the nodes in the tree, starting from the root, traversed in a *postorder* manner.

#     A postorder traversal visits the nodes in the following order: left child, right child, parent.

#     For example, a binary tree with the following structure:

#     ```plaintext
#             1
#           /    \
#          9      8
#         / \    / 
#        6   2  3
#     ```

#     Should output a python list: `[6, 2, 9, 3, 8, 1]`.

# todo: implement this
def postorder(tree):
    traversal = []
    def _postorder(node):
        if node is None:
            return
        _postorder(node.left)
        _postorder(node.right)
        traversal.append(node.key)
    _postorder(tree)
    return traversal
