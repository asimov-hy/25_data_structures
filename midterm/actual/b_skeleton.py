#### DO NOT MODIFY ####
class BinaryTree:
    class _Node:
        def __init__(self, key=None):
            self.key = key
            self.parent = None
            self.left = None
            self.right = None

    def __init__(self):
        self._root = None
        self._size = 0

    def add_root(self, key):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(key=key)
        return self._root

    def add_left(self, node, key):
        if node.left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node.left = self._Node(key=key)
        node.left.parent = node
        return node.left

    def add_right(self, node, key):
        if node.right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node.right = self._Node(key=key)
        node.right.parent = node
        return node.right

    def is_empty(self):
        return self._size == 0

    def root(self):
        return self._root

    def parent(self, node):
        return node.parent

    def left(self, node):
        return node.left

    def right(self, node):
        return node.right

    def children(self, node):
        children = []
        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)
        return children

    def num_children(self, node):
        count = 0
        if node.left:
            count += 1
        if node.right:
            count += 1
        return count

    def is_leaf(self, node):
        return self.num_children(node) == 0

    def is_root(self, node):
        return node == self._root

    def delete(self, node):
        if self.num_children(node) == 2:
            raise ValueError('Node has two children')
        child = node.left if node.left else node.right
        if child:
            child.parent = node.parent
        if node is self._root:
            self._root = child
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child
        self._size -= 1
        return child.key

    def __str__(self):
        def _pretty_print(root, level=0, prefix='Root: '):
            if root is None:
                return

            # print current node
            ret = ' ' * (level * 4) + prefix + f'{root.key}\n'
            if root.left is not None or root.right is not None:
                # print left subtree
                if root.left:
                    ret += _pretty_print(root.left, level + 1, 'L--- ')
                else:
                    ret += ' ' * ((level + 1) * 4) + 'L--- None\n'
                # print right subtree
                if root.right:
                    ret += _pretty_print(root.right, level + 1, 'R--- ')
                else:
                    ret += ' ' * ((level + 1) * 4) + 'R--- None\n'
            return ret

        return _pretty_print(self._root)

    def from_arr(self, arr):
        self._root = self._Node(key=arr[0])
        q = [self._root]
        i = 1
        while q and i < len(arr):
            node = q.pop(0)
            if arr[i] is not None:
                node.left = self._Node(key=arr[i])
                node.left.parent = node
                q.append(node.left)
            i += 1
            if i < len(arr) and arr[i] is not None:
                node.right = self._Node(key=arr[i])
                node.right.parent = node
                q.append(node.right)
            i += 1
        self._size = len(arr) if arr else 0
