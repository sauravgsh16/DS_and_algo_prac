''' Iterative DFS '''


class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for i in range(self.V)]

    def add_edge(self, src, dest):
        self.adj[src].append(dest)

    def DFS_Util(self, s, visited):
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

    def dfs(self):
        visited = [False] * self.V
        for i in range(self.V):
            if visited[i] == False:
                self.DFS_Util(i, visited)

g1 = Graph(5)
g1.add_edge(1, 0)
g1.add_edge(0, 2)
g1.add_edge(2, 1)
g1.add_edge(0, 3)
g1.add_edge(1, 4)
g1.dfs()