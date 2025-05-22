class Graph:
    def __init__(self, adj_matrix):
        self.data = {
            i: [j for j in range(len(adj_matrix[i])) if adj_matrix[i][j]]
            for i in range(len(adj_matrix))
        }

    def size(self):
        return sum(len(v) for v in self.data.values())

    def order(self):
        return len(self.data)

    def add_node(self, node):
        self.data.setdefault(node, list())

    def remove_node(self, node):
        if node in self.data:
            del self.data[node]
        for i in self.data.keys():
            self.remove_arc(i, node)

    def add_arc(self, source_node, target_node):
        self.add_node(source_node)
        self.add_node(target_node)
        if target_node not in self.data[source_node]:
            self.data[source_node].append(target_node)
            self.data[source_node].sort()

    def remove_arc(self, source_node, target_node):
        if source_node in self.data and target_node in self.data[source_node]:
            self.data[source_node].remove(target_node)


adj_matrix = [[0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
g = Graph(adj_matrix)
print(g.data)

print(g.size(), g.order())

g.remove_node(2)
print(g.data)

g.add_arc(3, 1)
g.add_arc(3, 0)
print(g.data)

g.remove_arc(0, 3)
g.remove_arc(0, 1)
print(g.data)
