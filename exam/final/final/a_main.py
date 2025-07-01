from io_handler import IOHandler
from a_skeleton import TreeMapSkeleton
from a1 import TreeMapBase1
from a2 import TreeMapBase2
from a3 import TreeMapBase3
from a4 import TreeMapBase4

INPUT_FILE = 'sample/a1.in'


#### DO NOT MODIFY ####
if __name__ == '__main__':
    ioh = IOHandler(input_file=INPUT_FILE)
    input_lines = ioh.read()

    output_data = []
    tm = TreeMapSkeleton()

    tm_type = input_lines[0].strip()
    if tm_type == 'base1':
        tm = TreeMapBase1()
    elif tm_type == 'base2':
        tm = TreeMapBase2()
    elif tm_type == 'base3':
        tm = TreeMapBase3()
    elif tm_type == 'base4':
        tm = TreeMapBase4()

    # initialization
    tm_initial = input_lines[1].strip().split(',')
    if tm_initial != ['']:
        tm_initial_arr = [(int(_k), int(_v)) for _k, _v in (x.split(':') for x in tm_initial)]
        tm._from_arr(tm_initial_arr)

    for line in input_lines[2:]:
        mode, *args = line.split()

        # problem a1
        if mode == 'search':
            s = tm._subtree_search(tm.root, int(args[0]))
            result = tm._subtree_search(s, int(args[1]))
            if result:
                output_data.append(str(result))

        # problem a2
        elif mode == 'upsert':
            tm[int(args[0])] = int(args[1])

        # problem a3
        elif mode == 'first':
            s = tm._subtree_search(tm.root, int(args[0]))
            result = tm._subtree_first_node(s)
            if result:
                output_data.append(str(result))

        # problem a4
        elif mode == 'after':
            s = tm._subtree_search(tm.root, int(args[0]))
            result = tm.after(s)
            if result:
                output_data.append(str(result))
            else:
                output_data.append('None')

        elif mode == 'print':
            output_data.append(str(tm))

    ## output
    output_str = '\n'.join(output_data)
    ioh.write(output_str)
