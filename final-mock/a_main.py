from io_handler import IOHandler
from a_skeleton import BinarySearchTreeSkeleton
from a1 import BinarySearchTree
from a2 import search, search_rank
from a3 import min_tree, max_tree
from a4 import delete  # ✅ Corrected: delete now comes from a4

INPUT_FILE = 'sample/a4.in'


#### DO NOT MODIFY ####
def test_bst(tree, command, data):
    if command == 'insert':
        tree.insert(int(data[0]))
        return tree, '-'
    elif command == 'delete':
        delete(tree, int(data[0]))  # ✅ use delete from a4
        return tree, '-'
    elif command == 'search':
        node = search(tree, int(data[0]))
        return tree, str(node.key) if node else 'None'
    elif command == 'search_rank':
        rank = search_rank(tree, int(data[0]))
        return tree, str(rank)
    elif command == 'min':
        result = min_tree(tree)
        return tree, str(result) if result is not None else 'None'
    elif command == 'max':
        result = max_tree(tree)
        return tree, str(result) if result is not None else 'None'
    elif command == 'print':
        return tree, str(tree)
    else:
        raise ValueError(f"Unknown command: {command}")


#### DO NOT MODIFY ####
if __name__ == '__main__':
    ioh = IOHandler(input_file=INPUT_FILE)
    input_lines = ioh.read()

    output_data = []
    tree = BinarySearchTree()

    for line in input_lines:
        parts = line.strip().split()
        if not parts:
            continue

        mode = parts[0]
        if mode != 'bst':
            raise ValueError(f"Unknown mode: {mode}")

        cmd = parts[1]
        args = parts[2:]
        _, result = test_bst(tree, cmd, args)
        if result != '-':
            output_data.append(result)

    output_str = '\n'.join(output_data)
    ioh.write(output_str)
