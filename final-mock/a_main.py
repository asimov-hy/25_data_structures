from io_handler import IOHandler
from a_skeleton import BinarySearchTreeSkeleton
from a1 import BinarySearchTree
from a2 import search

INPUT_FILE = 'sample/a2.in'


#### DO NOT MODIFY ####
def test_bst(tree, command, data):
    if command == 'insert':
        tree.insert(int(data[0]))
        return tree, '-'
    elif command == 'search':
        return tree, str(tree.search(int(data[0])))
    elif command == 'min':
        return tree, str(tree.min())
    elif command == 'max':
        return tree, str(tree.max())
    elif command == 'delete':
        tree.delete(int(data[0]))
        return tree, '-'
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

        mode = parts[0]  # e.g., 'bst'
        if mode != 'bst':
            raise ValueError(f"Unknown mode: {mode}")

        cmd = parts[1]
        args = parts[2:]
        _, result = test_bst(tree, cmd, args)
        if result != '-':
            output_data.append(result)

    output_str = '\n'.join(output_data)
    ioh.write(output_str)
