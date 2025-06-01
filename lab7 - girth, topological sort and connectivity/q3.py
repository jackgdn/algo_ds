def find_scc(adj_lists):
    n = len(adj_lists)
    adj_matrix = [[1 if v in adj_lists[u] else 0 for v in range(n)] for u in range(n)]
    topo = list(
        map(
            lambda x: x[0],
            sorted(enumerate(dfs(adj_matrix)), key=lambda x: x[1], reverse=True),
        )
    )

    reversed = [[1 if adj_matrix[v][u] else 0 for v in range(n)] for u in range(n)]
    scc = [-1] * n
    visited = [False] * n

    def dfs_scc(u, reversed, root):
        scc[u] = root
        visited[u] = True
        for v in range(n):
            if reversed[u][v] and not visited[v]:
                dfs_scc(v, reversed, root)

    for u in topo:
        if not visited[u]:
            dfs_scc(u, reversed, u)
    print(scc)


INF = float("inf")


def dfs(adj_matrix):
    n = len(adj_matrix)
    discovered_time = [INF] * n
    finished_time = [INF] * n
    time = 1

    tree, forward, back, cross = [], [], [], []

    def dfs_visit(curr_node):
        nonlocal time
        discovered_time[curr_node] = time
        time += 1
        for next_node in range(n):
            if adj_matrix[curr_node][next_node]:
                if discovered_time[next_node] == INF:
                    tree.append((curr_node, next_node))
                    dfs_visit(next_node)
                elif finished_time[next_node] == INF:
                    back.append((curr_node, next_node))
                elif discovered_time[curr_node] < discovered_time[next_node]:
                    forward.append((curr_node, next_node))
                else:
                    cross.append((curr_node, next_node))

        finished_time[curr_node] = time
        time += 1

    for node in range(n):
        if discovered_time[node] == INF:
            dfs_visit(node)

    return finished_time


find_scc([[3], [0], [0, 3, 4], [1], [2]])

find_scc([[2, 3], [0], [1], [4], []])

find_scc([[1], [2], [0]])

find_scc([[1], [2], [0], [4], [5], [0, 6], [2, 4], [5, 3]])

find_scc([[1, 2], [3], [3, 4], [0, 5], [5], []])
