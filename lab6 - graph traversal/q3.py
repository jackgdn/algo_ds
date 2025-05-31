from collections import deque

INF = float("inf")


def distance(adj_list, s):
    n = len(adj_list)
    dist = [INF] * n
    dist[s] = 0

    queue = deque()
    queue.append(s)

    while queue:
        curr_node = queue.popleft()
        for next_node in adj_list[curr_node]:
            if dist[next_node] == INF:
                dist[next_node] = dist[curr_node] + 1
                queue.append(next_node)

    return dist


adj_list = [[], [2, 3], [1, 4], [1], [2]]
d = distance(adj_list, 0)
print(d)
d = distance(adj_list, 2)
print(d)

adj_list = [[2, 4, 6], [4], [0, 4], [5], [0, 1, 2, 5], [3, 4], [0]]
d = distance(adj_list, 0)
print(d)

adj_list = [[], [2, 3], [1, 4], [1], [2]]
d = distance(adj_list, 0)
print(d)
d = distance(adj_list, 2)
print(d)

adj_list = [[4], [2, 3, 4], [1], [1], [0, 1]]
d = distance(adj_list, 0)
print(d)

adj_list = [[], [2], [1, 3], [2, 5, 6], [5], [3, 4], [3]]
d = distance(adj_list, 1)
print(d)
