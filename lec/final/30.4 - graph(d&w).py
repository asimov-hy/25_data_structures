class Graph:
    """Representation of a simple weighted, directed graph using an adjacency map."""

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
        """Lightweight edge structure for a weighted graph."""
        __slots__ = '_origin', '_destination', '_weight'

        def __init__(self, u, v, weight):
            # 1. Store origin, destination vertices and weight
            self._origin = u
            self._destination = v
            self._weight = weight

        def endpoints(self):
            # 1. Return (origin, destination) as a tuple
            return (self._origin, self._destination)

        def opposite(self, v):
            # 1. Given a vertex v, return the other endpoint of the edge
            return self._destination if v is self._origin else self._origin

        def weight(self):
            # 1. Return the weight stored in this edge
            return self._weight

        def __hash__(self):
            # 1. Make Edge hashable using a tuple of its endpoints
            return hash((self._origin, self._destination))

    def __init__(self, directed=True):
        # 1. Initialize the directed graph structure
        self._outgoing = {}  # maps each vertex to its outgoing edges
        self._incoming = {} if directed else self._outgoing
        self._directed = directed

    def is_directed(self):
        # 1. Return True if graph is directed
        return self._directed

    def vertex_count(self):
        # 1. Return the number of vertices in the graph
        return len(self._outgoing)

    def vertices(self):
        # 1. Return an iterable of all vertices in the graph
        return self._outgoing.keys()

    def edge_count(self):
        # 1. Count all edges (no double counting for directed)
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total

    def edges(self):
        # 1. Return a set of all edges in the graph
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        # 1. Return the edge from u to v, if it exists
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        # 1. Return number of edges incident to vertex v (outgoing or incoming)
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        # 1. Yield each edge incident to vertex v (outgoing or incoming)
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        # 1. Create a new Vertex with the given element
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self._directed:
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, weight=1.0):
        # 1. Create a new Edge with the given weight from u to v
        e = self.Edge(u, v, weight)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
        return e
