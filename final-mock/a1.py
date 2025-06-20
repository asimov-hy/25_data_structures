from a_skeleton import BinarySearchTreeSkeleton, Node

class BinarySearchTree(BinarySearchTreeSkeleton):
    def insert(self, key):
        # 1. Check if the tree is empty (root is None)
        if self.root is None:
            # If empty, create a new node and set it as root
            self.root = Node(key)
            return

        # 2. Start from the root node
        node = self.root
        while True:
            # 3. If the key to insert is less than the current node's key
            if key < node.key:
                # 3a. If there is a left child, move to the left child
                if node.left:
                    node = node.left
                else:
                    # 3b. If no left child, insert new node here
                    node.left = Node(key)
                    node.left.parent = node  # Set parent pointer for the new node
                    return
            else:
                # 4. If the key to insert is greater than or equal to the current node's key
                # 4a. If there is a right child, move to the right child
                if node.right:
                    node = node.right
                else:
                    # 4b. If no right child, insert new node here
                    node.right = Node(key)
                    node.right.parent = node  # Set parent pointer for the new node
                    return
