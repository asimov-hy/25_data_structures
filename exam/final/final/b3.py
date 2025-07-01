## Problem b3: Shortest Path    

# todo: Implement this -> djikstra method
def shortest_path(graph, start, end):
    d = {}        # distance map
    paths = []  # store paths
    # store multiple apths

    for v in graph.vertices():
        if v == source:
            d[v] = 0
        else:
            d[v] = float('inf')
        [v] = pq.add(v, d[v])

    while not pq.is_empty():
        u, dist = pq.remove_min()
        cloud[u] = dist

        for edge in graph.incident_edges(u):
            v = edge.opposite(u)
            if v not in cloud:
                weight = edge.element()
                if d[u] + weight < d[v]:
                    d[v] = d[u] + weight
                    pq.update(pq_locator[v], d[v])
