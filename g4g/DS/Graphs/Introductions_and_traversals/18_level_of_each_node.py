''' Level of each node in a Tree '''

from collections import defaultdict

class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def print_levels_BFS(self, src):
        visited = [False] * self.V
        level = [0] * self.V

        queue = []
        queue.append(src)

        visited[src] = True
        level[src] = 0

        while len(queue) > 0:
            s = queue.pop(0)

            for i in self.graph[s]:
                if visited[i] == False:
                    visited[i] = True
                    level[i] = level[s] + 1
                    queue.append(i)
        
        for n, l in enumerate(level):
            print '{} --> {}'.format(n, l)

g = Graph(8)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(1, 5)
g.add_edge(2, 5)
g.add_edge(2, 6)
g.add_edge(6, 7)

g.print_levels_BFS(0)
