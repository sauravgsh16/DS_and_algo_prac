''' Print all paths from src to destination using BFS in a directed graph '''

class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(self.V)]

    def edd_edge(self, src, dest):
        self.graph[src].append(dest)

    def find_paths(self, src):
        queue = []
        path = []
        path.append(src)
        queue.append(path)
