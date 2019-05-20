''' Depth First Traversal '''

'''
   Depth first traversal is similar to DFS in a tree. The only catch here is,
   unlike trees, graphs may contain cycles, so we may come to the same node
   again. To avoid processing a node more than once, we use a boolean visited
   array.
'''

from collections import defaultdict


class Graph_Inc(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def depth_first_util(self, v, visited):
        visited[v] = True
        print v,

        for i in self.graph[v]:
            if visited[i] == False:
                self.depth_first_util(i, visited)

    def depth_first_traversal(self, v):
        visited = [False] * len(self.graph)

        self.depth_first_util(v, visited)

# The above implementation will not traverse vertices which are not reachable
# from the given vertex. E.g. Disconnected graph
# Thus we must call the dfs_util for every node.

class Graph_Complete(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def dfs_util(self, v, visited):
        visited[v] = True
        print v,

        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_util(i, visited)

    def dfs(self):
        visited = [False] * self.V

        for i in range(self.V):
            if visited[i] == False:
                self.dfs_util(i, visited)


g = Graph_Complete(5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.dfs()