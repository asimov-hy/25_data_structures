# Problem a: Binary Search Tree

#### DO NOT MODIFY ####
class TreeMapSkeleton():
    class Node():
        def __init__(self, key, value, parent=None):
            self.key = key
            self.value = value
            self.parent = parent
            self.left = None
            self.right = None

        def __str__(self):
            return f'{self.key}:{self.value}'

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    # Problem a1: Searching for a Key
    def _subtree_search(self, node, key):
        raise NotImplementedError("Must be implemented in subclass")

    # Problem a2: Inserting or Updating a Node
    def __setitem__(self, key, value):
        raise NotImplementedError("Must be implemented in subclass")

    # Problem a3: Finding the Node with the Minimum Key
    def _subtree_first_node(self, node):
        raise NotImplementedError("Must be implemented in subclass")

    # Problem a4: What's Next?
    def after(self, node):
        raise NotImplementedError("Must be implemented in subclass")

    def __getitem__(self, key):
        if self.is_empty():
            raise KeyError(f'KeyError: {key}')

        node = self._subtree_search(self.root, key)
        return node

    def first(self):
        if self.is_empty():
            raise KeyError('KeyError: first')
        return self._subtree_first_node(self.root)

    def __str__(self):
        def _serialize(node):
            if node is None:
                return []
            return [node] + _serialize(node.left) + _serialize(node.right)
        serialized = _serialize(self.root)
        return ','.join([f'{node.key}:{node.value}' for node in serialized])
    
    def _from_arr(self, arr):
        nodes = []
        for idx, (k, v) in enumerate(arr):
            if idx == 0:
                r = self.Node(k, v)
                self.root = r
                nodes.append(r)
                continue
            if idx % 2 == 1:
                parent = nodes[(idx - 1) // 2]
                n = self.Node(k, v, parent)
                parent.left = n
                nodes.append(n)
            else:
                parent = nodes[(idx - 2) // 2]
                n = self.Node(k, v, parent)
                parent.right = n
                nodes.append(n)
        return



