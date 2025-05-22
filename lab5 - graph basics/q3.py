from collections import defaultdict


def reverse(adj_list):
    nodes = set()
    dd = defaultdict(list)
    for u in adj_list:
        for v in adj_list[u]:
            nodes.add(u)
            nodes.add(v)
            dd[v].append(u)
    return {u: sorted(dd[u]) for u in sorted(nodes)}


re = reverse({0: [1, 2, 3], 1: [3], 2: [3], 3: []})
print(re)
