''' Print all paths from src to destination using BFS in a directed graph '''

class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(self.V)]

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def find_paths(self, src, dest):
        path = []
        path.append(src)
        self.find_paths_util(src, dest, path)

    def find_paths_util(self, src, dest, path):
        if src == dest:
            print path
        
        for i in self.graph[src]:
            if i not in path:
                path.append(i)
                self.find_paths_util(i, dest, path)
                path.pop(path.index(i))
    
    def bfs(self, src, dest):
        visited = [False] * self.V
        distance = [0] * self.V
        queue = []

        queue.append(src)
        visited[src] = True
        distance[src] = 0

        # print self.graph

        while len(queue) > 0:
            s = queue.pop(0)
            for i in self.graph[s]:
                if not visited[i]:
                    visited[i] = True
                    distance[i] = distance[s] + 1
                    queue.append(i)

        print distance[dest]

g = Graph(4)
g.add_edge(0, 3)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 0)
g.add_edge(2, 1)

g.find_paths(2, 3)
g.bfs(2, 3)