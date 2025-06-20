#### DO NOT MODIFY ####
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTreeSkeleton:
    def __init__(self):
        self.root = None

    def insert(self, key):
        raise NotImplementedError()

    def search(self, key):
        raise NotImplementedError()

    def min(self):
        raise NotImplementedError()

    def max(self):
        raise NotImplementedError()

    def delete(self, key):
        raise NotImplementedError()

    def __str__(self):
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(str(node.key))
            inorder(node.right)

        inorder(self.root)
        return '[' + ', '.join(result) + ']'
