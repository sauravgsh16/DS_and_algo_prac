''' A Peterson graph problem '''

class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[False for _ in range(self.V)] for _ in range(self.V)]

    def add_edge(self, src, dest):
        self.graph[src][dest] = True
        self.graph[dest][src] = True


g = Graph(10)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 0)
g.add_edge(0, 5)
g.add_edge(1, 6)
g.add_edge(2, 7)
g.add_edge(3, 8)
g.add_edge(4, 9)
g.add_edge(5, 7)
g.add_edge(7, 9)
g.add_edge(9, 6)
g.add_edge(6, 8)
g.add_edge(8, 5)
