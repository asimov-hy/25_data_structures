# b2.py

def has_cycle(graph):
    """
    Detects if a directed graph contains a cycle.

    Returns:
        True if there is at least one cycle, False otherwise.
    """
    discovered = {}    # v -> True if visited
    parent = {}        # v -> parent of v in DFS tree
    stack = []         # path stack
    backtrack = []     # where the cycle path would be stored (optional)

    def cycle_dfs(v):
        discovered[v] = True
        stack.append(v)

        for edge in graph.incident_edges(v):
            u = edge.opposite(v)
            if u not in discovered:
                parent[u] = v
                if cycle_dfs(u):
                    return True
            elif u != parent.get(v):  # back edge found
                backtrack.extend(stack[stack.index(u):])
                return True

        stack.pop()
        return False

    for vertex in graph.vertices():
        if vertex not in discovered:
            if cycle_dfs(vertex):
                return True

    return False
