class DSU :
    """
        Disjoint Set Union (Union-Find)

        Operations:
        - find(x): returns representative of x (with path compression)
        - union(a, b): merges sets (union by size), returns True if merged, False if already same
        - connected(a, b): checks if in same set
        - component_size(x): size of component containing x

        Time complexity: ~ O(alpha(n)) per operation (almost constant)
    """

    def __init__(self , n) :
        if n <= 0 :
            raise ValueError("n must be positive")

        self.n = n
        self.parent = list(range(n))
        self.count = n
        self.rank = [0] * n
        self.size = [1] * n


    def _validate(self , u) :
        if not (0 <= u < self.n) :
            raise IndexError(f"u must be in range [0.{self.n - 1}]")

    def find(self, x):
        self._validate(x)
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False

        # attach smaller rank under bigger rank
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]  # keep component size
        self.count -= 1

        # increase rank only if ranks were equal
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

        return True


    def connected(self , x , y) :
        return self.find(x) == self.find(y)

    def component_size(self , u) :
        return self.size[self.find(u)]