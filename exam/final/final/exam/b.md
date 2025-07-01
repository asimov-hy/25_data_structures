# Problem b: Graph

A graph is a data structure that consists of a finite set of vertices (nodes) and a collection of edges that connect pairs of vertices.

The following are examples of two graphs:

```plaintext
Graph A:
    1
   / \
  2 - 3 - 5
 /     \
4       6
```

```plaintext
Graph B:
    1        5
   /          \
  2 - 3        6
 /            / \
4            7   8 - 9
```

In this problem, skeletons of the `Vertex` and `Edge` classes, as well as the (undirected)`Graph` class using an adjacency list representation are provided for you.

## Problem b1: Bredth-First Search (BFS)

(Medium, 8 points)

Breadth-First Search (BFS) is a fundamental algorithm for traversing or searching through graph data structures. In BFS, we start
 at a vertex and explore all its neighbors before moving on to the next level of vertices. For this, BFS classifies edges into 
 three types:

- `UNEXPLORED`: An edge that has not been explored yet.
- `DISCOVERY`: An edge that leads to a vertex that has not been visited yet.
- `CROSS`: An edge that connects two vertices that have already been visited.

Finish implementing the `bfs_v` function. The `bfs` function is already complete and should not be modified.

- `bfs_v(graph: Graph, v: Vertex)`: This function should perform a breadth-first search starting from the vertex `v`. 
- It should mark the vertex as `VISITED`, and explore all its adjacent vertices iteratively. 
- The function should also classify edges as `UNEXPLORED`, `DISCOVERY`, or `CROSS` based on the BFS traversal.

## Problem b2: Detecting a Cycle

(Easy, 5 points)

Implement the following function:

- `has_cycle(graph: Graph) -> bool`: This function should return `True` if the `graph` contains a cycle and `False` otherwise.

    For example, `has_cycle(graphA)` should return `True` since there is a cycle: 1 -> 2 -> 3 -> 1. On the other hand,
     `has_cycle(graphB)` should return `False` since there is no cycle in this graph.

    Hint: Use the BFS algorithm implemented in the previous problem. A cycle exists if you encounter a `CROSS` edge 
    during the BFS traversal.

## Problem b3: Shortest Path

(Medium, 8 points)

Implement the following function:

- `shortest_path(graph: Graph, start: Vertex, end: Vertex) -> int`: This function should return the length of the shortest path from the vertex `start` to the vertex `end`.

    If there is no path between the two vertices, the function should return `-1`.

For example, `shortest_path(graphA, Vertex 1, Vertex 6)` should return `2`, since the shortest path from vertex 1 to vertex 6 is: 1 -> 3 -> 6. On the other hand, `shortest_path(graphB, Vertex 1, Vertex 9)` should return `-1`, since there is no path from vertex 1 to vertex 9.
