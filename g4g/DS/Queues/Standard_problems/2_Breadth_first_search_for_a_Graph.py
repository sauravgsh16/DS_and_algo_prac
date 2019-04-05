''' Breadth first search (BSF) for a graph '''

from collections import defaultdict

class Graph(object):

    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, source):
        visited = [False] * len(self.graph)

        queue = []

        # Mark the source node as visited and enQueue it
        visited[source] = True
        queue.append(source)

        while queue:

            # Dequeue a vertex from the queue and print it
            s = queue.pop(0)
            print s

            # Get all the adjacent vertices of the deQueued vertex s.
            # If a adjacent has not been visited, then mark it visited and
            # enQueue it
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

g.BFS(2)
print g.graph
print len(g.graph)
