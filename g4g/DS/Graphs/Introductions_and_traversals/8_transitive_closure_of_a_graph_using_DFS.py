''' Transitive Closure of a graph using DFS '''

'''
   Given a directed graph, find out if vertex v is reachable from another vertex
   u, for all pairs of (u, v) is the given graph. Reachable here means that there
   is a path from vertex u to v.
   The reach-ability matrix is called transitive closure of the graph

   Below are abstract steps of algorithm.
   1) Create a matrix tc[V][V] that would finally have transitive closure of
      given graph. Initialize all entries of tc[][] as 0.
   2) Call DFS for every node of graph to mark reachable vertices in tc[][].
      In recursive calls to DFS, we don't call DFS for an adjacent vertex if
      it is already marked as reachable in tc[][]
'''

from collections import defaultdict

class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.tc = [[0 for i in range(self.V)] for j in range(self.V)]

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def DFS_util(self, s, v):
        self.tc[s][v] = 1

        for i in self.graph[v]:
            if self.tc[s][i] == 0:
                self.DFS_util(s, i)

    def transitive_closure(self):
        for i in range(self.V):
            self.DFS_util(i, i)
        print self.tc

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.transitive_closure()
