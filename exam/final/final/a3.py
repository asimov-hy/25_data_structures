from a2 import TreeMapBase2
## Problem a3: Finding the Node with the Minimum Key
## Problem a3: Finding the Node with the Minimum Key

# (Easy, 5 points)

# Implement the following function:

# - `_subtree_first_node(node: Node) -> Node`: This function takes a `node` as input and returns the node with the minimum key within the subtree rooted at the given `node`.

#     For example, `_subtree_first_node(self.root)` should return the node with key 1.

# todo: implement this
class TreeMapBase3(TreeMapBase2):
    def _subtree_first_node(self, node):
        # find leftmost node until no left child left
        current = node
        while current and current.left:
            current = current.left
        return current
