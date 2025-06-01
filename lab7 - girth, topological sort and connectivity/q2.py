def schedule(dep):
    n = len(dep)
    in_degree = list(map(len, dep))
    adj_list = [[] for _ in range(n)]
    processed = [False] * n
    for v in range(n):
        for u in dep[v]:
            adj_list[u].append(v)
    result = list()

    for _ in range(n):
        for u in range(n):
            if in_degree[u] == 0 and not processed[u]:
                result.append(u)
                processed[u] = True
                for v in adj_list[u]:
                    in_degree[v] -= 1
                break

    return result if len(result) == n else None


dep = [[4, 5], [3, 4], [5], [2], [], []]
print(schedule(dep))

dep = [[], [], [0, 1]]
print(schedule(dep))

dep = [[], [0], [0], [2, 5], [1], [1], [3, 4, 5]]
print(schedule(dep))

dep = [[1, 2], [3, 5], [3], [6, 7, 8], [5], [6, 9], [8], [8], [9], []]
print(schedule(dep))

dep = [[], [0, 3], [0], [2, 5], [1], [1], [3, 4, 5]]
print(schedule(dep))
