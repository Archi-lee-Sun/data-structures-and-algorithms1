from weighted_graph import WeightedGraph
import heapq


def dijkstra(graph , start) :

    dist = [float('inf')] * graph.n
    dist[start] = 0
    heap = [(0 , start)]


    while heap :
        curr_dist , u = heapq.heappop(heap)

        if curr_dist > dist[u] :
            continue

        for v , w in graph.neighbors(u) :
            if w < 0 :
                raise ValueError("Dijkstra cannot handle negative weights")

            if dist[u] + w < dist[v] :
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v] , v))



    return dist










