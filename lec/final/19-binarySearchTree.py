class BSTNode:
    def __init__(self, key, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

class BST:
    def __init__(self):
        self.root = None

# --------------------------- search ---------------------------

    def search(self, search_node):
        # 1. Set current node
        node = self.root
        # 2. Begin traversal
        while node:
            # 3. If match found
            if search_node == node.key:
                return node
            # 4. If search_node is smaller, go left
            if search_node < node.key:
                node = node.left
            # 5. If search_node is larger, go right
            else:
                node = node.right
        # 6. Not found
        return None
    
# --------------------------- insert ---------------------------

    def insert(self, target):
        # 1. Handle empty tree
        if not self.root:
            self.root = BSTNode(target)
            return
        
        # 2. Start traversal
        node = self.root
        while True:
            # 3. Go left if target is smaller
            if target < node.key:
                # 3-1. If left child exists, continue traversal
                if node.left: node = node.left
                else:
                # 3-2. If left child does not exist, insert
                    node.left = BSTNode(target, node)
                    return
                
            # 4. Go right if target is larger or equal
            else:
                # 4-1. If right child exists, continue traversal
                if node.right: node = node.right
                # 4-2. If right child does not exist, insert
                else:
                    node.right = BSTNode(target, node)
                    return
                
# --------------------------- delete ---------------------------

    def delete(self, target):
        # 1. Find the node to delete
        node = self.search(target)
        if not node:
            return False

        # 2. Case: node has a right child
        if node.right:
            # 2-1. Find the in-order successor (leftmost of right subtree)
            successor = node.right
            while successor.left:
                successor = successor.left

            # 2-2. Copy successor's key to current node
            node.key = successor.key

            # 2-3. Delete the successor node
            # if successor has a right child
            if successor.right:
                # if succesor is left child of its parent
                if successor == successor.parent.left:
                    # replace the left child
                    successor.parent.left = successor.right
                
                # if successor is right child of its parent
                else:
                    successor.parent.right = successor.right

                # update the parent of the right child
                successor.right.parent = successor.parent
            
            # if successor has no right child
            else:
                # if successor is left child of its parent
                if successor == successor.parent.left:
                    # remove the left child
                    successor.parent.left = None
                # if successor is right child of its parent
                else:
                    # remove the right child
                    successor.parent.right = None

        # 3. Case: node has only a left child (no right subtree)
        # if node has a left child
        elif node.left:
            # if node is root
            if node.parent is None:
                # replace root with left child
                self.root = node.left
            # if node is left child of its parent
            elif node == node.parent.left:
                # replace left child with left child
                node.parent.left = node.left
            # if node is right child of its parent
            else:
                # replace right child with left child
                node.parent.right = node.left
            
            # update the parent of the left child
            node.left.parent = node.parent

        # 4. Case: node has no children
        else:
            # if node is root, set root to None
            if node.parent is None:
                self.root = None
            
            # if node is left child of its parent
            elif node == node.parent.left:
                node.parent.left = None
            # else node is right child of its parent
            else:
                node.parent.right = None

        return True

    
# --------------------------- traversal ---------------------------

    # preorder: Root -> Left -> Right
    def preorder(self, node=None):
        if node is None: node = self.root
        if node:
            print(node.key, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)
    
    # postorder: Left -> Right -> Root
    def postorder(self, node=None):
        if node is None: node = self.root
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=' ')

    # inorder: Left -> Root -> Right
    def inorder(self, node=None):
        if node is None: node = self.root
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)
