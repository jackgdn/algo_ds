from collections import deque


def is_reachable(adj_matrix, s, d):
    n = len(adj_matrix)
    visited = [False] * n
    stack = deque()
    visited[s] = True
    stack.append(s)

    while stack:
        curr_node = stack.pop()
        if curr_node == d:
            return True
        for next_node in range(n):
            if adj_matrix[curr_node][next_node] and not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)
    return False


adj_matrix = [[0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]]
print(is_reachable(adj_matrix, 0, 3))
print(is_reachable(adj_matrix, 3, 0))

adj_matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
]
print(is_reachable(adj_matrix, 4, 4))
print(is_reachable(adj_matrix, 0, 2))

adj_matrix = [
    [0, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
]
print(is_reachable(adj_matrix, 0, 3))
print(is_reachable(adj_matrix, 1, 2))

adj_matrix = [
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
]
print(is_reachable(adj_matrix, 4, 2))
print(is_reachable(adj_matrix, 1, 3))
print(is_reachable(adj_matrix, 4, 3))
