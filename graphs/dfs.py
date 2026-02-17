from graph import Graph

def dfs(graph : Graph , start : int) :
    visited = [False] * graph.n
    result = []
    graph._validate_vertex(start)

    def _dfs(u) :
        visited[u] = True
        result.append(u)

        for v in graph.neighbors(u) :
            if not visited[v] :
                _dfs(v)


    _dfs(start)
    return result


