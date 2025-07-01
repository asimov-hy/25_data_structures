from a3 import TreeMapBase3
# Problem a4: What's next?
# - `after(node: Node) -> Node`: 
#       This function takes a `node` as input and returns the next node in the in-order traversal of the binary search tree. 
#       If the given `node` is the last node in the traversal, the function should return `None`.

#     For example, `after(self.root)` should return the node with key 6, while `after(self.root.left)` 
#           should return the node with key 4, and `after(self.root.right)` should return `None`.

#     Hint: Here are the rules for finding the next node in the in-order traversal:

#     1. If the given node has a right child, the next node in the in-order traversal is the leftmost node of the right subtree.

#     2. Otherwise, you should traverse the parent nodes until you find a node that is the left child of its parent. 
#           This parent will be the next node in the in-order traversal.

#         - Note that the parent of the root node is `None`, so you should stop traversing when you reach the root node.

class TreeMapBase4(TreeMapBase3):
    # todo: implement this
    def after(self, node):
        # 1: If node has a right child, return the leftmost node in right subtree
        if node.right:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr

        # Rule 2: Go up until we find a node that is a left child of its parent
        curr = node
        while curr.parent and curr == curr.parent.right:
            curr = curr.parent
        return curr.parent  # May be None if node is the last in-order node

# # 1. traversal function
# def inorder(self, visited, node=None):
#     if node is None: 
#         node = self.root
#     if node:
#         self.inorder(node.left)
#         list.append(node.key, end=' ')
#         self.inorder(node.right)


# # lsit for keep tracking of traversal
# visited = []
# inorder(visited, node)
# return visited[len(visited)-1]