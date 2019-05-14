''' Breadth First Traversal or Breadth First Search '''

'''
   BFS of a graph is similar to BFS of a tree. Only catch here is, unlike trees,
   graphs may contain cycles, so we may come across the same node again.
   To avoid processing the same node again we use a boolean visited array.
'''

from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def breadth_first_traversal(self, s):
        visited = [False] * len(self.graph)
        # Queue for BFS
        queue = []
        # Append source node to queue
        queue.append(s)
        visited[s] = True

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

g.breadth_first_traversal(2)
