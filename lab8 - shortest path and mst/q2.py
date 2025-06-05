def dijkstra(adj_matrix, s):
    n = len(adj_matrix)
    dist = [float("inf")] * n
    dist[s] = 0
    paths = [None] * n
    paths[s] = [s]
    visited = [False] * n
    for _ in range(n):
        u = min_distance(dist, visited)
        if dist[u] == float("inf"):
            break
        visited[u] = True
        for v in range(n):
            if adj_matrix[u][v] > 0 and not visited[v]:
                alt = dist[u] + adj_matrix[u][v]
                if alt < dist[v]:
                    dist[v] = alt
                    paths[v] = paths[u] + [v]
    return dist, paths


def min_distance(dist, visited):
    min_val = float("inf")
    min_index = -1
    for i in range(len(dist)):
        if not visited[i] and dist[i] < min_val:
            min_val = dist[i]
            min_index = i
    return min_index


adj_matrix = [
    [0, 3, 8, 0, 0],
    [2, 0, 0, 2, 0],
    [0, 1, 0, 7, 2],
    [0, 3, 2, 0, 5],
    [0, 0, 0, 0, 0],
]
dist, paths = dijkstra(adj_matrix, 0)
print(dist)
print(paths)

adj_matrix = [
    [0, 3, 1, 0, 0],
    [3, 0, 7, 5, 1],
    [1, 7, 0, 2, 0],
    [0, 5, 2, 0, 7],
    [0, 1, 0, 7, 0],
]
dist, paths = dijkstra(adj_matrix, 2)
print(dist)
print(paths)

adj_matrix = [
    [0, 1, 4, 0, 0],
    [0, 0, 2, 7, 0],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
]
dist, paths = dijkstra(adj_matrix, 0)
print(dist)
print(paths)

adj_matrix = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 2, 0, 2, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2, 3],
    [0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0],
]
dist, paths = dijkstra(adj_matrix, 0)
print(dist)
print(paths)

adj_matrix = [
    [0, 1, 0, 0, 0],
    [0, 0, 7, 0, 2],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 1, 0],
]
dist, paths = dijkstra(adj_matrix, 0)
print(dist)
print(paths)
