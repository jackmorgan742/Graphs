class Graph_ES:
    def __init__(self, V=None, E=None):
        self.edges = set()
        self.vertices = set()
        if V is not None:
            self.vertices.update(V)
        if E is not None:
            self.edges.update(E)

    def add_vertex(self, v):
        self.vertices.add(v)

    def remove_vertex(self, v):
        self.vertices.remove(v)
        self.edges = {(u,w) for (u,w) in self.edges if u!=v and w!=v}

    def add_edge(self, e):
        self.edges.add(e)
        self.vertices.update(e)

    def remove_edge(self, e):
        self.edges.remove(e)

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices)

    def _neighbors(self, v):
        return (w for (u,w) in self.edges if u==v)

class Graph_AS:
    def __init__(self, V=None, E=None):
        self.adj = {}
        if V is not None:
            for v in V:
                self.add_vertex(v)
        if E is not None:
            for e in E:
                self.add_edge(e)

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = set()

    def remove_vertex(self, v):
        if v in self.adj:
            del self.adj[v]
            for u in self.adj:
                self.adj[u].discard(v)

    def add_edge(self, e):
        u, v = e
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].add(v)

    def remove_edge(self, e):
        u, v = e
        self.adj[u].discard(v)

    def __len__(self):
        return len(self.adj)

    def __iter__(self):
        return iter(self.adj)

    def _neighbors(self, v):
        return iter(self.adj[v])
    