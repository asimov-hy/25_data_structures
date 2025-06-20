"""
Breadth-First Search (BFS) for Graph Traversal
----------------------------------------------

Function:
- `BFS(graph, start_vertex, discovery_tree)`:
  1. Begins at `start_vertex`.
  2. Explores the graph level by level using a queue-like structure.
  3. For each newly discovered vertex, records the edge that led to it in `discovery_tree`.

Notes:
- `discovery_tree` maps each vertex to the edge used to discover it.
- The root `start_vertex` should be pre-mapped to `None` before calling.
- Operates in-place; useful for building shortest-path trees in unweighted graphs.
"""


def BFS(graph, start_vertex, discovery_tree):
    """
    Perform BFS traversal of the graph starting at start_vertex.
    
    Parameters:
        graph           -- the Graph object
        start_vertex    -- the starting Vertex
        discovery_tree  -- dict: maps each discovered vertex to the edge that discovered it
                           (start_vertex should already be in the dictionary mapped to None)

    This function modifies discovery_tree in-place.
    """
    current_level = [start_vertex]   # First layer includes only the start vertex

    while current_level:
        next_level = []              # Prepare to gather newly discovered vertices

        for u in current_level:
            for edge in graph.incident_edges(u):
                v = edge.opposite(u)
                if v not in discovery_tree:     # If this neighbor hasn't been discovered
                    discovery_tree[v] = edge    # Mark edge that discovered vertex v
                    next_level.append(v)        # Add v to next layer

        current_level = next_level              # Move to the next BFS level

#-----------------------------------------------------------------

