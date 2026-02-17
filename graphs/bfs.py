from graph import Graph
from collections import deque

def bfs(graph : Graph , start : int ) :

    visited = [False] * graph.n
    queue = deque([start])
    visited[start] = True

    order = []

    while queue :
        u = queue.popleft()
        order.append(u)

        for v in graph.neighbors(u) :
            if not visited[v] :
                queue.append(v)
                visited[v] = True

    return order