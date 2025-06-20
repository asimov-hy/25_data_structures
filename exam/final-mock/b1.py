# b1.py

def dfs(graph, start):
    """
    Returns a list of vertices in the order they are visited by DFS.
    Uses a discovery map to simulate tree traversal.
    """
    result = []
    discovery_map = {start: None}

    def DFS(graph, start_vertex, discovery_map):
        for edge in graph.incident_edges(start_vertex):
            neighbor = edge.opposite(start_vertex)
            if neighbor not in discovery_map:
                discovery_map[neighbor] = edge
                result.append(neighbor)
                DFS(graph, neighbor, discovery_map)

    result.append(start)
    DFS(graph, start, discovery_map)
    return result


def bfs(graph, start):
    """
    Returns a list of vertices in the order they are visited by BFS.
    Uses a discovery tree (dict) as output from BFS traversal.
    """
    result = []
    discovery_tree = {start: None}

    def BFS(graph, start_vertex, discovery_tree):
        current_level = [start_vertex]
        while current_level:
            next_level = []
            for u in current_level:
                for edge in graph.incident_edges(u):
                    v = edge.opposite(u)
                    if v not in discovery_tree:
                        discovery_tree[v] = edge
                        next_level.append(v)
            current_level[:] = next_level

    result.append(start)
    BFS(graph, start, discovery_tree)
    for node in discovery_tree:
        if node != start:
            result.append(node)
    return result
