from a1 import BinarySearchTree

# a2.py

def search(tree, key):
    # 1. Start at the root of the tree.
    node = tree.root
    # 2. Traverse the tree until the node is None (key not found).
    while node:
        # 3. If the current node's key matches the search key, return the node.
        if key == node.key:
            return node 
        # 4. If the search key is less than the current node's key, go left.
        elif key < node.key:
            node = node.left
        # 5. If the search key is greater, go right.
        else:
            node = node.right
    # 6. If the key is not found, return None.
    return None




# -------------------------------------------------
# a2.py

def search_rank(tree, key):
    # 1. Helper function to count the number of nodes in a subtree rooted at n.
    def count(n):
        if n is None:
            return 0
        return 1 + count(n.left) + count(n.right)

    # 2. Start at the root of the tree.
    node = tree.root
    # 3. Initialize rank to 0. This will store the number of nodes less than the key.
    rank = 0

    # 4. Traverse the tree to search for the key.
    while node:
        # 5. If the current node's key matches the search key:
        if key == node.key:
            # 6. If the node has a left subtree, add its node count to rank.
            if node.left:
                rank += count(node.left)
            # 7. Return the rank (number of nodes less than the key).
            return rank
        # 8. If the search key is less than the current node's key, go left.
        elif key < node.key:
            node = node.left
        # 9. If the search key is greater than the current node's key:
        else:
            # 10. Increment rank by 1 for the current node.
            rank += 1
            # 11. If the node has a left subtree, add its node count to rank.
            if node.left:
                rank += count(node.left)
            # 12. Move to the right child.
            node = node.right

    # 13. If the key is not found, return -1.
    return -1
