from a_skeleton import BinarySearchTreeSkeleton, Node

class BinarySearchTree(BinarySearchTreeSkeleton):
    def insert(self, key):
        # 1. check if the tree is empty
        if self.root is None:
            # 2. If empty, create a new root node
            self.root = Node(key)
            return

        # 2. Start traversal from the root
        node = self.root
        while True:
            # 3. Go left if target is smaller
            if key < node.key:
                # 3-1. If left child exists, continue traversal
                if node.left: node = node.left
                else:
                # 3-2. If left child does not exist, insert
                    node.left = Node(key)
                    return
                
            # 4. Go right if target is larger or equal
            else:
                # 4-1. If right child exists, continue traversal
                if node.right: node = node.right
                # 4-2. If right child does not exist, insert
                else:
                    node.right = Node(key)
                    return
        pass
