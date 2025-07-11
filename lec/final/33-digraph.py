"""
Topological Sort (DFS-based) for Directed Acyclic Graphs (DAGs)
---------------------------------------------------------------

Function:
- `topological_sort(graph)`:
  1. Performs DFS on each unvisited vertex.
  2. Appends each vertex after fully exploring its descendants (post-order).
  3. Reverses the result to produce a valid topological ordering.

Returns:
- A list of vertices in topologically sorted order.

Note:
- Assumes input is a directed acyclic graph (DAG).
- Handles disconnected graphs by initiating DFS from all unvisited nodes.
"""


def topological_sort(graph):
    """
    Return a list of vertices in topologically sorted order (only for DAGs).
    
    Parameters:
        graph -- a directed Graph instance

    Returns:
        A list of Vertex objects in topological order
    """
    topo_order = []      # 1. Will store the topological order
    visited = set()      # 2. Track visited vertices

    def dfs(vertex):
        visited.add(vertex)  # 3. Mark current vertex as visited
        # 4. Visit all unvisited neighbors (edges point from vertex to neighbor)
        for edge in graph.incident_edges(vertex):
            neighbor = edge.opposite(vertex)
            if neighbor not in visited:
                dfs(neighbor)  # 5. Recursive DFS call
        topo_order.append(vertex)  # 6. Add to topo_order after visiting descendants (post-order)

    # 7. Start DFS from each unvisited vertex (handles disconnected graphs)
    for v in graph.vertices():
        if v not in visited:
            dfs(v)

    topo_order.reverse()  # 8. Reverse post-order to get correct topological sort
    return topo_order      # 9. Return the sorted list
