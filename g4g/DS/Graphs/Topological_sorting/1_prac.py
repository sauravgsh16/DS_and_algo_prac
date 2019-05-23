''' Topological Sort '''
from collections import defaultdict

class Graph(object):
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)
        print stack

    def topological_sort_util(self, src, visited, stack):
        visited[src] = True

        for i in self.graph[src]:
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)
        
        stack.insert(0, src)


g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

g.topological_sort()