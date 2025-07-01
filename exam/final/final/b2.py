from b1 import bfs
# ## Problem b2: Detecting a Cycle

# (Easy, 5 points)

# Implement the following function:

# - `has_cycle(graph: Graph) -> bool`: This function should return `True` if the `graph` contains a cycle and `False` otherwise.

#     For example, `has_cycle(graphA)` should return `True` since there is a cycle: 1 -> 2 -> 3 -> 1. On the other hand,
#      `has_cycle(graphB)` should return `False` since there is no cycle in this graph.

#     Hint: Use the BFS algorithm implemented in the previous problem. A cycle exists if you encounter a `CROSS` edge 
#     during the BFS traversal.


# todo: Implement this
def has_cycle(graph):

    # reset unexplored - from b1
    for v in graph.vertices():
        v.label = "UNEXPLORED"
    for e in graph.edges():
        e.label = "UNEXPLORED"

    # being looking for cycle
    for v in graph.vertices():
        # if vertice is unexplored
        if v.label == "UNEXPLORED":
            
            # traverse bfs - 했으면 사용해야지
            bfs(graph, v)

            # for every incidnet edge
            for e in graph.incident_edges(v):
                
                # cross = met -> cycle
                if e.label == "CROSS":
                    return True
    
    # no cycle
    return False
    
