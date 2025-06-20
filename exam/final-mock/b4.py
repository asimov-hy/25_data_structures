# b4.py

from adaptable_priority_queue import AdaptablePriorityQueue  # You must provide this class

def dijkstra(graph, source):
    """
    Compute shortest-path distances from source to all reachable vertices.
    
    Parameters:
        graph  -- a Graph instance with weighted edges
        source -- starting vertex (must support element())
    
    Returns:
        A dictionary mapping each reachable vertex to its shortest-path distance
    """
    d = {}        # tentative distance map: vertex -> distance
    cloud = {}    # finalized shortest distances: vertex -> distance
    pq = AdaptablePriorityQueue()
    pq_locator = {}  # vertex -> PQ entry

    # 1. Initialize distances
    for v in graph.vertices():
        if v == source:
            d[v] = 0
        else:
            d[v] = float('inf')
        pq_locator[v] = pq.add(v, d[v])

    # 2. Main loop
    while not pq.is_empty():
        u, dist = pq.remove_min()
        cloud[u] = dist  # finalize distance for u

        for edge in graph.incident_edges(u):
            v = graph.opposite(u, edge)
            if v not in cloud:
                weight = edge.element()
                if d[u] + weight < d[v]:
                    d[v] = d[u] + weight
                    pq.update(pq_locator[v], d[v])

    return {v.element(): dist for v, dist in cloud.items()}
