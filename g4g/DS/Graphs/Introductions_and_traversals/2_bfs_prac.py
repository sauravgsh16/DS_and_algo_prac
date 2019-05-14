from collections import defaultdict

class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def bfs(self, src):
        visited = [False] * len(self.graph)
        queue = []
        queue.append(src)
        visited[src] = True
        while queue:
            s = queue.pop(0)
            print s,
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.bfs(2)
