from collections import defaultdict


def induced(adj_list, node_list):
    result = defaultdict(list)
    for u in node_list:
        if u not in adj_list:
            continue
        for v in node_list:
            if v in adj_list[u]:
                result[u].append(v)
        result[u].sort()
    return dict(result)


result = induced({0: [1], 1: [0, 4], 2: [3, 4], 3: [2], 4: [0, 1, 2, 3]}, [1, 2, 3])
print(result)
