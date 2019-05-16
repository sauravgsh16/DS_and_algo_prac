''' Minimum number of edges between vertices '''

class Graph(object):
    def __init__(self, V):
        self.V = V
        self.graph = [[] for _ in range(self.V)]

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def find_min_edges(self, src, dest):
        path = []
        path.append(src)
        count = [2**32]
        self.find_min_edges_util(src, dest, path, count)
        print count[0]

    def find_min_edges_util(self, src, dest, path, count):
        ''' Personal solution '''
        if src == dest:
            if count[0] > len(path) - 1:
                count[0] = len(path) - 1
        
        for i in self.graph[src]:
            if i not in path:
                path.append(i)
                self.find_min_edges_util(i, dest, path, count)
                path.pop(path.index(i))

    def find_edge_min(self, src, dest):
        ''' Solution according to G4G '''
        visited = [False] * self.V
        distance = [0] * self.V

        queue = []
        queue.append(src)
        visited[src] = True
        distance[src] = 0

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

g.find_min_edges(2, 3)
g.find_edge_min(2, 3)
