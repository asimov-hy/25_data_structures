from a1 import BinarySearchTree

def delete(tree, target):
    # 1. Find the node to delete
    node = tree.root
    while node and node.key != target:
        if target < node.key:
            node = node.left
        else:
            node = node.right

    if not node:
        return False

    # 2. Case: node has a right child
    if node.right:
        # 2-1. Find in-order successor (leftmost of right subtree)
        successor = node.right
        while successor.left:
            successor = successor.left

        # 2-2. Copy successor's key to current node
        node.key = successor.key

        # 2-3. Delete the successor node
        if successor.right:
            if successor == successor.parent.left:
                successor.parent.left = successor.right
            else:
                successor.parent.right = successor.right
            successor.right.parent = successor.parent
        else:
            if successor == successor.parent.left:
                successor.parent.left = None
            else:
                successor.parent.right = None

    # 3. Case: node has only left child
    elif node.left:
        if node.parent is None:
            tree.root = node.left
        elif node == node.parent.left:
            node.parent.left = node.left
        else:
            node.parent.right = node.left
        node.left.parent = node.parent

    # 4. Case: node has no children
    else:
        if node.parent is None:
            tree.root = None
        elif node == node.parent.left:
            node.parent.left = None
        else:
            node.parent.right = None

    return True
