from collections import deque

INF = float("inf")


def find_girth(adj_list):
    n = len(adj_list)
    min_girth = INF

    for start in range(n):
        dist = [INF] * n
        dist[start] = 0
        parent = [-1] * n
        queue = deque()
        queue.append(start)

        while queue:
            curr_node = queue.popleft()
            for next_node in adj_list[curr_node]:
                if dist[next_node] == INF:
                    dist[next_node] = dist[curr_node] + 1
                    parent[next_node] = curr_node
                    queue.append(next_node)
                elif parent[curr_node] != next_node:
                    min_girth = min(min_girth, dist[next_node] + dist[curr_node] + 1)

    return min_girth


adj_list = [[1, 2], [0, 4, 5], [0, 3], [2, 5, 6], [1, 6], [1, 3, 6], [3, 4, 5]]
print(find_girth(adj_list))

adj_list = [[2], [3], [0, 3], [1, 2, 4, 5], [3], [3]]
print(find_girth(adj_list))

adj_list = [[1, 2], [0, 4, 5], [0, 3], [2, 5, 6], [1, 6], [1, 3, 6], [3, 4, 5]]
print(find_girth(adj_list))

adj_list = [[1, 5], [0, 2], [1, 3], [2, 4], [3, 5], [0, 4]]
print(find_girth(adj_list))

adj_list = [[1, 2, 3], [0, 2], [0, 1, 4], [0, 4], [2, 3]]
print(find_girth(adj_list))
