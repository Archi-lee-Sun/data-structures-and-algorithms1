
class WeightedGraph :
    def __init__(self , n , directed = False) :
        if n <= 0 :
            raise ValueError("n must be positive")
        self.n = n
        self.directed = directed
        self.adj = [[] for _ in range(n)]



    def _validate_vertex(self , vertex) :
        if not (0 <= vertex < self.n) :
            raise ValueError(f"Vertex {vertex} must be in range [0, {self.n - 1}]")


    def add_edge(self ,  u , v , w) :
        self._validate_vertex(u)
        self._validate_vertex(v)

        if not isinstance(w , (int , float)) :
            raise TypeError("Weight must be an integer or float")

        self.adj[u].append((v,w))

        if not self.directed :
            self.adj[v].append((u,w))


    def neighbors(self , u) :
        """Return list of (v, w) edges out of u."""
        self._validate_vertex(u)

        return self.adj[u]

    def edges(self) :

        res = []

        if self.directed :
            for u in range(self.n) :
                for v , w in self.adj[u] :
                    res.append((u,v,w))
        else :
            for u in range(self.n) :
                for v , w in self.adj[u] :
                    if v > u :
                        res.append((u,v,w))

        return res


