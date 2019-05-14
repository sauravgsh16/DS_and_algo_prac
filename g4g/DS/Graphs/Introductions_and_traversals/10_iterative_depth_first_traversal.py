''' Iterative Depth First Traversal '''

from collections import defaultdict

class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def dfs(self, s):
        visited = [False] * self.V

        stack = []
        stack.append(s)

        while len(stack) != 0:
            s = stack.pop()

            if visited[s] == False:
                print s,
                visited[s] = True
            
            for i in self.graph[s]:
                if visited[i] == False:
                    stack.append(i)

# Above implementation print only vertices that are reachable from given vertex.
# DFS to print all vertices is as below:

class GraphComplete(object):
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for i in range(self.V)]

    def add_edge(self, src, dest):
        self.adj[src].append(dest)

    def DFS_util(self, s, visited):
        stack = []
        stack.append(s)
    
        while len(stack) != 0:
            s = stack.pop()
            if visited[s] == False:
                print s,
                visited[s] = True
            
            i = 0
            while i < len(self.adj[s]):
                if visited[self.adj[s][i]] == False:
                    stack.append(self.adj[s][i])
                i += 1

    def depth_first_search(self):
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                self.DFS_util(i, visited)


g1 = Graph(5)
g1.add_edge(1, 0)
g1.add_edge(0, 2)
g1.add_edge(2, 1)
g1.add_edge(0, 3)
g1.add_edge(1, 4)
g1.dfs(0)

print '\n'
g2 = GraphComplete(5)
g2.add_edge(1, 0)
g2.add_edge(0, 2)
g2.add_edge(2, 1)
g2.add_edge(0, 3)
g2.add_edge(1, 4)
g2.depth_first_search()
