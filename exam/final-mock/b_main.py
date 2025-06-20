from io_handler import IOHandler
from b_skeleton import Graph
from b1 import dfs, bfs
from b2 import has_cycle
from b3 import topological_sort
from b4 import dijkstra

INPUT_FILE = 'sample/b_test.in'

def test_graph(graph, command, args):
    if command == "dfs":
        start = args[0]
        return str(dfs(graph, start))
    elif command == "bfs":
        start = args[0]
        return str(bfs(graph, start))
    elif command == "has_cycle":
        return str(has_cycle(graph))
    elif command == "topsort":
        return str(topological_sort(graph))
    elif command == "dijkstra":
        start = args[0]
        return str(dijkstra(graph, start))
    else:
        raise ValueError(f"Unknown command: {command}")

if __name__ == '__main__':
    ioh = IOHandler(input_file=INPUT_FILE)
    input_lines = ioh.read()

    output_data = []
    g = Graph(directed=False)  # default to undirected, may switch to directed inside

    for line in input_lines:
        tokens = line.strip().split()
        if not tokens:
            continue

        if tokens[0] == "add_edge":
            _, u, v, *rest = tokens
            weight = int(rest[0]) if rest else 1
            g.add_edge(u, v, weight)

        elif tokens[0] == "directed":
            g.directed = True  # make the graph directed

        elif tokens[0] == "undirected":
            g.directed = False

        else:
            mode, *args = tokens
            result = test_graph(g, mode, args)
            if result:
                output_data.append(result)

    ioh.write('\n'.join(output_data))
