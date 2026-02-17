class Graph :
    def __init__(self , n , directed = False) :
        if n <= 0 :
            raise ValueError("n must be positive")

        self.n = n
        self.directed = directed
        self.adj = [[] for _ in range(n)]


    def _validate_vertex(self , u) :
        if not (0 <= u < self.n) :
            raise ValueError(f"Vertex {u} must be in range [0,{self.n - 1}]")


    def add_edge(self , u , v):
        self._validate_vertex(u)
        self._validate_vertex(v)


        self.adj[u].append(v)

        if not self.directed :
            self.adj[v].append(u)


    def has_edge(self , u , v) :
        self._validate_vertex(u)
        self._validate_vertex(v)

        return v in self.adj[u]

    def neighbors(self , u) :
        self._validate_vertex(u)
        return self.adj[u]


    def degree(self , u) :
        self._validate_vertex(u)
        return len(self.adj[u])

    def __repr__(self):
        lines = []
        for i in range(self.n) :
            lines.append(f"{i}: {self.adj[i]}")

        return "\n".join(lines)


