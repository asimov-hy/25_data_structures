def DFS(graph, start_vertex, discovery_map):
    """
    Perform DFS traversal on the undiscovered portion of the graph starting at 'start_vertex'.

    Parameters:
        graph         -- the Graph object (must support incident_edges and opposite methods)
        start_vertex  -- the starting Vertex of the DFS
        discovery_map -- dictionary mapping each discovered vertex to the edge that discovered it

    Side Effects:
        Populates 'discovery_map' with all reachable vertices from start_vertex.
    """
    for edge in graph.incident_edges(start_vertex):    # for every edge connected to the vertex
        adjacent = edge.opposite(start_vertex)          # get the neighboring vertex
        if adjacent not in discovery_map:               # if the vertex hasn't been discovered
            discovery_map[adjacent] = edge              # mark how it was discovered
            DFS(graph, adjacent, discovery_map)         # recurse on the neighbor

def DFS(graph, start_vertex, visited=None):
    """
    Perform DFS traversal from 'start_vertex', marking visited vertices.

    Parameters:
        graph         -- the Graph object
        start_vertex  -- the starting Vertex
        visited       -- set of visited vertices (optional, created if not provided)
    """
    if visited is None:
        visited = set()

    visited.add(start_vertex)
    for edge in graph.incident_edges(start_vertex):
        neighbor = edge.opposite(start_vertex)
        if neighbor not in visited:
            DFS(graph, neighbor, visited)

# ------------------------------------------------------------

def path_dfs(graph, v, goal, discovered, path):
    """Modified DFS to find path from v to goal."""
    discovered[v] = True
    path.append(v)

    if v == goal:
        return True

    for e in graph.incident_edges(v):
        u = e.opposite(v)
        if u not in discovered:
            if path_dfs(graph, u, goal, discovered, path):
                return True

    path.pop()
    return False


# ------------------------------------------------------------------

def cycle_dfs(graph, v, discovered, parent, stack, backtrack):
    """Modified DFS to find any simple cycle."""
    discovered[v] = True
    stack.append(v)

    for e in graph.incident_edges(v):
        u = e.opposite(v)
        if u not in discovered:
            parent[u] = v
            if cycle_dfs(graph, u, discovered, parent, stack, backtrack):
                return True
        elif u != parent[v]:  # Found a back edge
            # Build the cycle from current stack
            backtrack.extend(stack[stack.index(u):])
            return True

    stack.pop()
    return False
