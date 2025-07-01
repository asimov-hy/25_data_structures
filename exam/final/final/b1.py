## Problem b1: Bredth-First Search (BFS)

# (Medium, 8 points)

# Breadth-First Search (BFS) is a fundamental algorithm for traversing or searching through graph data structures. In BFS, we start
#  at a vertex and explore all its neighbors before moving on to the next level of vertices. For this, BFS classifies edges into 
#  three types:

# - `UNEXPLORED`: An edge that has not been explored yet.
# - `DISCOVERY`: An edge that leads to a vertex that has not been visited yet.
# - `CROSS`: An edge that connects two vertices that have already been visited.

# Finish implementing the `bfs_v` function. The `bfs` function is already complete and should not be modified.

# - `bfs_v(graph: Graph, v: Vertex)`: This function should perform a breadth-first search starting from the vertex `v`. 
# - It should mark the vertex as `VISITED`, and explore all its adjacent vertices iteratively. 
# - The function should also classify edges as `UNEXPLORED`, `DISCOVERY`, or `CROSS` based on the BFS traversal.

# todo: Implement this
def bfs_v(graph, v):

    # 1.  discovery tree init
    discovery = {v: None}  
    # 2. start with first vertex
    current_level = [v]


    while current_level:
        # store newl vertices
        next_level = []          

        for node in current_level:
            # Mark the current vertex as visited
            node.label = "VISITED" 
            
            # explore incident edges of vertices
            for edge in graph.incident_edges(node):
                v = edge.opposite(node)
                
                # If neighbor undiscovered
                if v not in discovery:  

                    # Classify edge as DISCOVERY
                    edge.label = "DISCOVERY"
                    # Mark edge
                    discovery[v] = edge  
                    
                    # Add v to next layer
                    next_level.append(v) 

                else:
                    # If alreayd has been found -> CROSS
                    edge.label = "CROSS"       

        current_level = next_level          # Move next level
















#### DO NOT MODIFY ####
def bfs(graph):
    for v in graph.vertices():
        v.label = "UNEXPLORED"
    for e in graph.edges():
        e.label = "UNEXPLORED"
    for v in graph.vertices():
        if v.label == "UNEXPLORED":
            bfs_v(graph, v)
