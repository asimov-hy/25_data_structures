class Graph:
    def __init__(self, directed=False):
        self.adj = {}  # maps node -> list of (neighbor, weight)
        self.directed = directed

    def add_edge(self, u, v, weight=1):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append((v, weight))

        if not self.directed:
            if v not in self.adj:
                self.adj[v] = []
            self.adj[v].append((u, weight))

    def vertices(self):
        return self.adj.keys()

    def incident_edges(self, u):
        return self.adj.get(u, [])

    def opposite(self, u, edge):
        # edge is (v, weight)
        return edge[0]

    def edge_weight(self, u, v):
        for neighbor, weight in self.adj.get(u, []):
            if neighbor == v:
                return weight
        return None
