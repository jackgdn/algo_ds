def Kruskal(adj_matrix):
    adj_list = list()
    n = len(adj_matrix)
    for u in range(n):
        for v in range(n):
            if adj_matrix[u][v]:
                adj_list.append((adj_matrix[u][v], u, v))

    adj_list.sort()

    pre = [i for i in range(n + 1)]
    res_adj = [[0 for _ in range(n)] for _ in range(n)]

    def find(u):
        nonlocal pre
        if pre[u] != u:
            pre[u] = find(pre[u])
        return pre[u]

    length = 0
    while adj_list:
        w, u, v = adj_list.pop(0)
        pu, pv = find(u), find(v)
        if pu != pv:
            pre[pu] = pv
            length += w
            res_adj[u][v] = w
            res_adj[v][u] = w

    return res_adj, length


adj_matrix = [[0, 1, 0, 0], [1, 0, 2, 3], [0, 2, 0, 3], [0, 3, 3, 0]]
res_adj, length = Kruskal(adj_matrix)
print(res_adj)
print(length)
