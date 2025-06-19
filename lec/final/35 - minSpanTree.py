def prim_jarnik_mst(graph):
    """
    Compute a minimum spanning tree of a connected, weighted, undirected graph.
    
    Parameters:
        graph -- an undirected, weighted Graph instance
    
    Returns:
        A list of edges in the MST
    """
    mst = []                             # list of edges in the MST
    d = {}                               # vertex -> min edge weight
    pq = AdaptablePriorityQueue()        # priority queue of (weight, vertex)
    pq_locator = {}                      # vertex -> pq item
    tree_edges = {}                      # vertex -> edge that connects it to the MST

    # pick any starting vertex
    for vertex in graph.vertices():
        d[vertex] = 0
        break

    for v in graph.vertices():
        if v != vertex:
            d[v] = float('inf')
        pq_locator[v] = pq.add(v, d[v])

    while not pq.is_empty():
        u, _ = pq.remove_min()
        if u in tree_edges:
            mst.append(tree_edges[u])
        
        for edge in graph.incident_edges(u):
            v = edge.opposite(u)
            if v in pq_locator:  # only consider vertices still in the queue
                weight = edge.element()
                if weight < d[v]:  # better connection found
                    d[v] = weight
                    tree_edges[v] = edge
                    pq.update(pq_locator[v], d[v])

    return mst

#--------------------------------------------

# Set up a graph
G = Graph(directed=False)
a = G.insert_vertex("A")
b = G.insert_vertex("B")
c = G.insert_vertex("C")
d = G.insert_vertex("D")

G.insert_edge(a, b, 4)
G.insert_edge(a, c, 1)
G.insert_edge(b, c, 3)
G.insert_edge(b, d, 2)
G.insert_edge(c, d, 5)

# Run Prim's algorithm
mst_edges = prim_jarnik_mst(G)
print("Minimum Spanning Tree:")
for edge in mst_edges:
    u, v = edge.endpoints()
    print(f"{u.element()} -- {v.element()} (weight {edge.element()})")
