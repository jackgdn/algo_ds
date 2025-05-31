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

    return map(sorted, (tree, forward, back, cross))


adj_matrix = [[0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
tree, forward, back, cross = dfs(adj_matrix)
print("Tree arcs: {}".format(tree))
print("Forward arcs: {}".format(forward))
print("Back arcs: {}".format(back))
print("Cross arcs: {}".format(cross))

adj_matrix = [[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0]]
tree, forward, back, cross = dfs(adj_matrix)
print("Tree arcs: {}".format(tree))
print("Forward arcs: {}".format(forward))
print("Back arcs: {}".format(back))
print("Cross arcs: {}".format(cross))

adj_matrix = [
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
]
tree, forward, back, cross = dfs(adj_matrix)
print("Tree arcs: {}".format(tree))
print("Forward arcs: {}".format(forward))
print("Back arcs: {}".format(back))
print("Cross arcs: {}".format(cross))

adj_matrix = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
tree, forward, back, cross = dfs(adj_matrix)
print("Tree arcs: {}".format(tree))
print("Forward arcs: {}".format(forward))
print("Back arcs: {}".format(back))
print("Cross arcs: {}".format(cross))
