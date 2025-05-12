## Problem b3: Depth of a Node


# todo: implement this
def depth(tree, key):
        if tree.is_root(key):
            return 0
        else:
            return 1 + depth(tree, tree.parent(tree, key))
