from a_skeleton import TreeMapSkeleton
# Problem a1: Searching for a Key

## Problem a1: Searching for a Key

# Finish implementing the `TreeMapBase1` class. 
#     Currently, the `_subtree_search` method is not fully implemented. 
#     Implement this method to complete the `TreeMapBase1` class.

# - `_subtree_search(self, node: Node, key: int) -> Node`: 
#         This function takes a `node` and a `key` to find as input 
#         and returns the `node` with the specified `key` if it exists within the subtree rooted at the given `node`.

    # If the specified `key` does not exist within the subtree, the function should return the node where the search ended 
    # (i.e., the node where the key should be inserted).

    # For example, in the tree above, `_subtree_search(self.root, 4)` 
    # should return the node with key 4, 
    # while `_subtree_search(self.root, 2)` is unable to find the key 2 and should return the node with key 1.




class TreeMapBase1(TreeMapSkeleton):
    # todo: implement this
    def _subtree_search(self, node, key):

        # empty node
        if node is None:
            return None
        
        # found key val
        if key == node.key:
            return node
        
        # if key is smaller -> go left
        elif key < node.key:
            if node.left is not None:
                return self._subtree_search(node.left, key)
            else:
                return node
        
        # else go right
        else:
            if node.right is not None:
                return self._subtree_search(node.right, key)
            else:
                return node


        # print(f"node: {node.value} key = {key}")

        # 1. set current node
        # node = self.root

        # # 2. begin traversal
        # while node:
        #     # 3. if match found
        #     if node.key == key:
        #         return node
        #     # 4. If search_node is smaller, go left
        #     if node.key < key:
        #         node = node.left
        #     # 5. If search_node is larger, go right
        #     else:
        #         node.key = node.right

        # # 6. node is not found
        # if node.key < key:
        #     return node.left
        # else:
        #     return node.right