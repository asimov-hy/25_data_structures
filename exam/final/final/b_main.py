from io_handler import IOHandler
from b_skeleton import Graph
from b1 import bfs
from b2 import has_cycle
from b3 import shortest_path

INPUT_FILE = 'sample/b1.in'


#### DO NOT MODIFY ####
if __name__ == '__main__':
    ioh = IOHandler(input_file=INPUT_FILE)
    input_lines = ioh.read()

    output_data = []
    graph = Graph()

    # initialization
    v_initial = input_lines[0].strip().split(',')
    for v in v_initial:
        graph.insert_vertex(int(v))
    e_initial = input_lines[1].strip().split(',')
    for e in e_initial:
        key1, key2 = e.split('-')
        u = graph.get_vertex(int(key1))
        v = graph.get_vertex(int(key2))
        graph.insert_edge(u, v)

    for line in input_lines[2:]:
        mode, *args = line.split()

        # problem b1
        if mode == 'bfs':
            bfs(graph)
            discovery_edges = []
            cross_edges = []
            for e in graph.edges():
                if e.label == "DISCOVERY":
                    discovery_edges.append(str(e))
                elif e.label == "CROSS":
                    cross_edges.append(str(e))
            print(f'DISCOVERY: {", ".join(discovery_edges)}')
            print(f'CROSS: {", ".join(cross_edges)}')

        # problem b2
        elif mode == 'cycle':
            if has_cycle(graph):
                output_data.append('YES')
            else:
                output_data.append('NO')

        # problem b3
        elif mode == 'shortest':
            s = graph.get_vertex(int(args[0]))
            e = graph.get_vertex(int(args[1]))
            result = shortest_path(graph, s, e)
            output_data.append(str(result))

        elif mode == 'print':
            print(graph)

    ## output
    output_str = '\n'.join(output_data)
    ioh.write(output_str)
