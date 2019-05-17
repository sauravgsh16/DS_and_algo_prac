''' Detect an cycle in an undirected graph '''

'''
   We use DFS to detect presense of any cycles.
   For every vertex 'v', if there is an adjacent vertex 'u' such that, u is
   already visited, and the parent of 'u' is not 'v', then a cycle exists.
'''
from collections import defaultdict

class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def is_cyclic(self):
        visited = [False] * self.vertices

        for i in self.graph:
            if not visited[i]:
                if self.is_cyclic_util(i, visited, -1) == True:
                    return True
        return False

    def is_cyclic_util(self, src, visited, parent):
        visited[src] = True

        for i in self.graph[src]:
            if not visited[i]:
                if self.is_cyclic_util(i, visited, src) == True:
                    return True
            # If adjacent vertex is visited and not parent of current vertex,
            # then a cycle exists
            elif parent != i:
                return True
        return False

g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 0)
g.add_edge(0, 3)
g.add_edge(3, 4)

print g.is_cyclic()

g1 = Graph(3)
g1.add_edge(0, 1)
g1.add_edge(1, 2)

print g1.is_cyclic()
