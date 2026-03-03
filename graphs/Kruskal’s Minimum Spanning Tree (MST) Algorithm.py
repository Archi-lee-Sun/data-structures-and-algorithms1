from dsu import DSU

def kruskal_mst(V , edges) :
    edges = sorted(edges, key = lambda e : e[2])

    dsu = DSU(V)
    cnt = 0
    cost = 0
    res = []

    for u , v , w in edges :
        if dsu.union(u,v) :
            cost += w
            cnt += 1
            res.append([u,v,w])

        if cnt == V - 1 :
            break

    if cnt != V - 1 :
        raise ValueError("Graph is disconnected; MST does not exist.")


    return (cost , res)


if __name__ == '__main__':
    edges = [[0, 1, 10], [1, 3, 15], [2, 3, 4], [2, 0, 6], [0, 3, 5]]
    print(kruskal_mst(4, edges))

