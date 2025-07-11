"""
Dijkstra’s Shortest Path Algorithm
----------------------------------

Function:
- `shortest_path_lengths(graph, source)`:
  1. Initializes all distances from `source` to ∞, except 0 for the source.
  2. Uses an Adaptable Priority Queue (min-heap) to explore the closest vertex.
  3. For each neighbor, updates distance if a shorter path is found.
  4. Finalized distances are stored in `cloud`.

Returns:
- A dictionary mapping each reachable vertex to its shortest-path distance from the source.

Assumes:
- All edge weights are non-negative.
- Graph supports `incident_edges(v)`, `opposite(v)`, and `element()` for weights.
"""


def shortest_path_lengths(graph, source):
    """
    Compute shortest-path distances from source to all reachable vertices.
    
    Parameters:
        graph  -- a Graph instance
        source -- starting Vertex
    
    Returns:
        A dictionary mapping reachable Vertex -> shortest distance from source
    """
    d = {}        # distance map
    cloud = {}    # map of known shortest distances
    pq = AdaptablePriorityQueue()
    pq_locator = {}

    for v in graph.vertices():
        if v == source:
            d[v] = 0
        else:
            d[v] = float('inf')
        pq_locator[v] = pq.add(v, d[v])

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

    return cloud

# --------------------------------------------------------

# Example setup
G = Graph(directed=False)
a = G.insert_vertex("A")
b = G.insert_vertex("B")
c = G.insert_vertex("C")
d = G.insert_vertex("D")

G.insert_edge(a, b, 1)
G.insert_edge(b, c, 2)
G.insert_edge(a, d, 4)
G.insert_edge(c, d, 1)

# Run Dijkstra
result = shortest_path_lengths(G, a)
for v, dist in result.items():
    print(f"Distance from A to {v.element()} = {dist}")
