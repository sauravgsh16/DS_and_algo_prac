from collections import defaultdict

class Graph(object):

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def breadth_fisrt_traversal(self, source):
        visited = [False] * len(self.graph)
        queue = []
        visited[source] = True
        queue.append(source)

        while queue:
            s = queue.pop(0)
            print s
            for i in self.graph[s]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.breadth_fisrt_traversal(2)