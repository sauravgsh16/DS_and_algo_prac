''' Topological Sorting '''

'''
   Topological sorting for Directed Acyclic Graph is a liner ordering of
   vertives such that, for every directed edge, uv, vertex u comes before v
   in the ordering. Topological sort is not possible is the graph is not a DAG.

   The first vertex of a topological sort is always a vertex with in-degree as 0,
   i.e.: a vertex with no incoming edges.

   Topological sorting is different from DFS. In topological sort we need to print
   the vertex before its adjacent vertex.

   Algorithm to find Topological Sorting:
   We recommend to first see implementation of DFS here. We can modify DFS to find
   Topological Sorting of a graph. In DFS, we start from a vertex, we first print it
   and then recursively call DFS for its adjacent vertices. In topological sorting,
   we use a temporary stack. We don't print the vertex immediately, we first recursively
   call topological sorting for all its adjacent vertices, then push it to a stack.
   Finally, print contents of stack. Note that a vertex is pushed to stack only when all
   of its adjacent vertices (and their adjacent vertices and so on) are already in stack.
'''

from collections import defaultdict

class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def topological_sort_util(self, src, visited, stack):
        visited[src] = True

        for i in self.graph[src]:
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)

        # **** NOTE ***
        # We need to insert the element at the beginning of the stack
        stack.insert(0, src)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)
        print stack

g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

g.topological_sort()
