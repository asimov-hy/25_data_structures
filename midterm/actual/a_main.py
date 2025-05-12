from io_handler import IOHandler
from a_skeleton import HeapSkeleton
from a1 import HeapBase
from a2 import Heap
from a3 import heap_sort

INPUT_FILE = 'sample/a3.in'


#### DO NOT MODIFY ####
def test_heap(h, command, data):
    if command == 'init':
        h._from_arr([int(x) for x in data])
        return h, '-'
    elif command == 'upheap':
        h._upheap(int(data[0]))
        return h, '-'
    elif command == 'downheap':
        h._downheap(int(data[0]))
        return h, '-'
    elif command == 'add':
        h.add(int(data[0]))
        return h, '-'
    elif command == 'remove_min':
        try:
            min_value = h.remove_min()
            return h, str(min_value)
        except Exception as _:
            return h, 'error'
    elif command == 'is_empty':
        return h, 'True' if h.is_empty() else 'False'
    elif command == 'len':
        return h, str(len(h))
    elif command == 'print':
        return h, str(h)
    else:
        raise ValueError(f"Unknown command: {command}")


#### DO NOT MODIFY ####
if __name__ == '__main__':
    ioh = IOHandler(input_file=INPUT_FILE)
    input_lines = ioh.read()

    output_data = []
    h = HeapSkeleton()

    heap_type = input_lines[0].strip()
    if heap_type == 'base':
        h = HeapBase()
    elif heap_type == 'heap':
        h = Heap()

    for line in input_lines[1:]:
        mode, *args = line.split()

        # problem a1 & a2
        if mode == 'heap':
            command, *data = args
            default_heap, result = test_heap(h, command, data)
            if result:
                output_data.append(result)

        # problem a3
        elif mode == 'sort':
            arr = [int(x) for x in args]
            sorted_arr = heap_sort(arr)
            output_data.append(str(sorted_arr))

    ## output
    output_str = '\n'.join(output_data)
    ioh.write(output_str)
