"""
Adjacency Map Graph Implementation
----------------------------------

Classes:
- `Vertex`: Represents a graph node with an associated element.
- `Edge`: Represents a connection between two vertices, with optional data.
- `Graph`: Directed or undirected graph using adjacency maps for storage.

Key Methods:
- `insert_vertex(x)`: Adds a new vertex with element x.
- `insert_edge(u, v, x)`: Adds an edge from vertex u to vertex v with optional element x.
- `get_edge(u, v)`: Returns the edge from u to v if it exists.
- `incident_edges(v)`: Iterates over all edges connected to vertex v.
- `vertices()`, `edges()`: Return all vertices or edges.
- `vertex_count()`, `edge_count()`: Return counts of vertices and edges.
- `degree(v)`: Returns number of incident edges (outgoing by default).
- `is_directed()`: Checks if the graph is directed.

Design:
- Uses hashable Vertex objects as dictionary keys.
- For undirected graphs, outgoing and incoming maps are aliased.
"""

class Graph:
    """Representation of a simple graph using an adjacency map."""

    class Vertex:
        """Lightweight vertex structure for a graph."""
        __slots__ = '_element'

        def __init__(self, x):
            # 1. Store the element associated with this vertex
            self._element = x

        def element(self):
            # 1. Return the element stored in this vertex
            return self._element

        def __hash__(self):
            # 1. Make Vertex hashable using its unique id (used as dictionary key)
            return hash(id(self))

    class Edge:
        """Lightweight edge structure for a graph."""
        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, u, v, x):
            # 1. Store origin and destination vertices and associated element
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            # 1. Return (origin, destination) as a tuple
            return (self._origin, self._destination)

        def opposite(self, v):
            # 1. Given a vertex v, return the other endpoint of the edge
            return self._destination if v is self._origin else self._origin

        def element(self):
            # 1. Return the element stored in this edge
            return self._element

        def __hash__(self):
            # 1. Make Edge hashable using a tuple of its endpoints
            return hash((self._origin, self._destination))

    def __init__(self, directed=False):
        # 1. Initialize the graph structure
        self._outgoing = {}              # 2. Maps each vertex to its outgoing edges
        self._directed = directed        # 3. Set whether graph is directed
        if directed:
            # 4. Create a separate incoming map for directed graphs
            self._incoming = {}
        else:
            # 5. For undirected graphs, use same map for incoming and outgoing
            self._incoming = self._outgoing

    def is_directed(self):
        # 1. Return True if graph is directed, otherwise False
        return self._directed

    def vertex_count(self):
        # 1. Return the number of vertices in the graph
        return len(self._outgoing)

    def vertices(self):
        # 1. Return an iterable of all vertices in the graph
        return self._outgoing.keys()

    def edge_count(self):
        # 1. Count all edges in the graph
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # 2. For undirected graphs, divide by 2 to avoid double counting
        return total if self._directed else total // 2

    def edges(self):
        # 1. Create a set to hold unique edges
        result = set()
        # 2. Add each edge from the adjacency maps to the set
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        # 1. Return the edge from vertex u to vertex v, if it exists
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        # 1. Choose the appropriate adjacency map based on direction
        adj = self._outgoing if outgoing else self._incoming
        # 2. Return the number of adjacent edges for vertex v
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        # 1. Choose the appropriate adjacency map
        adj = self._outgoing if outgoing else self._incoming
        # 2. Yield each incident edge from the vertex
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        # 1. Create a new Vertex with the given element
        v = self.Vertex(x)
        # 2. Add it to the outgoing map
        self._outgoing[v] = {}
        # 3. If graph is directed, also add to incoming map
        if self._directed:
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        # 1. Create a new Edge between u and v with optional element x
        e = self.Edge(u, v, x)
        # 2. Register the edge in the outgoing map of u
        self._outgoing[u][v] = e
        # 3. Register the edge in the incoming map of v
        self._incoming[v][u] = e
        return e
