from a1 import TreeMapBase1
## Problem a2: Inserting or Updating a Node


class TreeMapBase2(TreeMapBase1):
    # todo: implement this
    def __setitem__(self, key, value):


        # 1. empty tree
        if self.is_empty():
            self.root = self.Node(key, value)
            return

        # 1. search for node
        node = self._subtree_search(self.root, key)


        
        # 2. if exist update
        if node.key == key:
            node.value = value

        # 3. else create new
        elif key < node.key:
            node.left = self.Node(key, value, parent=node)
        else:
            node.right = self.Node(key, value, parent=node)
        
        pass
