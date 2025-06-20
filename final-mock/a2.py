from a1 import BinarySearchTree

def search(self, key):
    # TODO: Implement search logic
    # 1. Set current node
    node = self.root
    # 2. Begin traversal
    while node:
        # 3. If match found
        if key == node.key:
            return node
        # 4. If search_node is smaller, go left
        if key < node.key:
            node = node.left
        # 5. If search_node is larger, go right
        else:
            node = node.right
    # 6. Not found
    return None





BinarySearchTree.search = search


# -------------------------------------------------

def search(self, key):
    node = self.root
    rank = 0

    while node:
        if key == node.key:
            # If left subtree exists, add its size (number of nodes < key)
            if node.left:
                # Count all nodes in left subtree
                def count(n):
                    if n is None:
                        return 0
                    return 1 + count(n.left) + count(n.right)
                rank += count(node.left)
            return rank

        elif key < node.key:
            node = node.left
        else:
            # Node.key < key → count this node and all in its left subtree
            rank += 1
            if node.left:
                def count(n):
                    if n is None:
                        return 0
                    return 1 + count(n.left) + count(n.right)
                rank += count(node.left)
            node = node.right

    # Not found
    return -1
