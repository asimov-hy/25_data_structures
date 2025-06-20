from io_handler import IOHandler
from b_skeleton import BinaryTree
from b1 import preorder
from b2 import postorder
from b3 import depth
from b4 import uncle
from b5 import max_path_sum

INPUT_FILE = 'sample/b2.in'


#### DO NOT MODIFY ####
if __name__ == '__main__':
    ioh = IOHandler(input_file=INPUT_FILE)
    input_lines = ioh.read()

    output_data = []
    b_tree = BinaryTree()
    b_tree.from_arr([int(x) for x in input_lines[0].split()])

    for line in input_lines[1:]:
        mode, *args = line.split()
        if mode == 'print':
            output_data.append(str(b_tree))

        # Problem b1
        elif mode == 'preorder':
            traversal = preorder(b_tree)
            output_data.append(str(traversal))

        # Problem b2
        elif mode == 'postorder':
            traversal = postorder(b_tree)
            output_data.append(str(traversal))

        # Problem b3
        elif mode == 'depth':
            key = int(args[0])
            node_depth = depth(b_tree, key)
            output_data.append(str(node_depth))

        # Problem b4
        elif mode == 'uncle':
            key = int(args[0])
            uncle_key = uncle(b_tree, key)
            output_data.append(str(uncle_key))

        # Problem b5
        elif mode == 'max_path_sum':
            max_sum = max_path_sum(b_tree)
            output_data.append(str(max_sum))

    ## output
    output_str = '\n'.join(output_data)
    ioh.write(output_str)
