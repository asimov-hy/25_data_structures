# Problem b: Graph

#### DO NOT MODIFY ####
class Vertex:
    def __init__(self, key):
        self.key = key
        self.label = None

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self):
        return f'{self.key}'

#### DO NOT MODIFY ####
class Edge:
    def __init__(self, u, v):
        self.origin = u
        self.destination = v
        self.label = None

    def opposite(self, v):
        return self.destination if v is self.origin else self.origin

    def __str__(self):
        return f'{self.origin.key}-{self.destination.key}'

#### DO NOT MODIFY ####
class Graph:
    def __init__(self):
        self.outgoing = {}
        self.incoming = self.outgoing  # undirected graph

    def vertices(self):
        return self.outgoing.keys()

    def edges(self):
        result = set()
        for secondary_map in self.outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_vertex(self, key):
        for v in self.vertices():
            if v.key == key:
                return v
        return None

    def get_edge(self, u, v):
        return self.outgoing[u].get(v)

    def incident_edges(self, v, outgoing=True):
        adj = self.outgoing if outgoing else self.incoming
        return adj[v].values()

    def insert_vertex(self, key):
        v = Vertex(key)
        self.outgoing[v] = {}
        return v

    def insert_edge(self, u, v):
        e = Edge(u, v)
        self.outgoing[u][v] = e
        self.outgoing[v][u] = e
        return e

    def __str__(self):
        ret = 'vertices: ' + ', '.join([str(v) for v in self.vertices()]) + '\n'
        ret += 'edges: ' + ', '.join([str(e) for e in self.edges()]) + '\n'
        return ret