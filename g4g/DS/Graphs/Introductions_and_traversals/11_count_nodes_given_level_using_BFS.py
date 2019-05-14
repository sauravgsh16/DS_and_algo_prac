''' Count the number of nodes at a given level in a tree using BFS '''

from collections import defaultdict

class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def BFS(self, s, levelcount):
        visited = [False] * self.V
        level = [0] * self.V
        queue = []
        queue.append(s)

        visited[s] = True
        level[s] = 0

        while len(queue) > 0:
            s = queue.pop(0)

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    level[i] = level[s] + 1
                    visited[i] = True
        count = 0
        for i in range(self.V):
            if level[i] == levelcount:
                count += 1
        return count

g = Graph(6)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)

print g.BFS(0, 2)
  