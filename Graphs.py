
import heapq

class Graph:

    def __init__(self, _V=(), E=()):
        """
        Initialize a new graph with vertex set _V and edge set _E
        """
        self._V = _V
        self._E = E
        self.adj_list = {v: {} for v in _V}
        for u, v, wt in E:
            self.add_edge(u, v, wt)


    def add_vertex(self, v):
        """
        Add a new vertex to the graph. The new vertex is identified with the v object
        """
        if v not in self.adj_list:
            self._V.append(v)
            self.adj_list[v] = set()


    def remove_vertex(self, v):
        """
        Remove the vertex v from the graph
        """
        self._V.remove(v)
    
        # Remove all edges that involve the vertex
        self._E = [e for e in self._E if v not in (e[0], e[1])]
        
        # Update the neighbor lists of other vertices
        for w in self._V:
            if v in self.adj_list[w]:
                del self.adj_list[w]


    def add_edge(self, u, v, wt):
        """
        Add a new edge to the graph between the vertices with keys u and v
        """
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u][v] = wt
        self.adj_list[v][u] = wt
            

    def remove_edge(self, u, v):
        """
        Remove the edge u,v from the graph
        """
        if v in self.adj_list[u]:
            del self.adj_list[u][v]
            del self.adj_list[v][u]
            self._E = [e for e in self._E if e[0] != u or e[1] != v]


    def nbrs(self, v):
        """
        Return an iterable collection of the (out)neighbors of v, i.e.
        those vertices w such that (v, w) is an edge
        """
        return self.adj_list[v].keys()


    def fewest_flights(self, city):
        """
        Finds the shortest number of flights to get from one city to any other city in the graph
        Returns a dictionary tree showing traversal order and a dictionary of vertex:distance pairs.
        """
        dist = {city: 0}
        prev = {city: None}
        visited = set()
        pq = [(0, city)]

        while pq:
            (d, u) = heapq.heappop(pq)
            if u in visited:
                continue
            visited.add(u)

            for v in self.nbrs(u):
                if v not in visited:
                    alt = dist[u] + 1
                    if v not in dist or alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u
                        heapq.heappush(pq, (alt, v))

        return prev, dist


    def shortest_path(self, city):
        """
        Finds the shortest path from the given city to all other cities in the graph based on distance.
        Returns a dictionary tree showing traversal order and a dictionary of vertex:distance pairs.
        """
        # Initialize data structures
        dist = {v: float('inf') for v in self._V}
        dist[city] = 0
        prev = {}
        heap = [(0, city)]
        
        # Dijkstra's algorithm
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v in self.adj_list[u]:
                w = self.adj_list[u][v]
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    heapq.heappush(heap, (dist[v], v))
        
        # Build dictionary tree and return results
        tree = {city: set()}
        for v in prev:
            if v != city:
                tree.setdefault(prev[v], set()).add(v)
        return tree, dist


    def minimum_salt(self, city):
        """
        Connect city to every other city in the graph with the fewest total number of miles
        Returns a dictionary tree showing traversal order and a dictionary of vertex:distance pairs.
        """
        distance = {v: float('inf') for v in self._V}
        parent = {v: None for v in self._V}
        heap = []
        visited = set()

        distance[city] = 0
        heapq.heappush(heap, (0, city))

        while heap:
            (dist, v) = heapq.heappop(heap)

            if v in visited:
                continue

            visited.add(v)

            for w in self.nbrs(v):
                new_dist = dist + self.adj_list[v][w]

                if new_dist < distance[w]:
                    distance[w] = new_dist
                    parent[w] = v
                    heapq.heappush(heap, (new_dist, w))

        # Construct the traversal order dictionary-tree
        traversal_order = {}
        for v in self._V:
            path = []
            while v is not None:
                path.append(v)
                v = parent[v]
            path.reverse()
            traversal_order[path[0]] = path

        return traversal_order, distance