''' Find if a path exists between 2 vertices in a directed graph '''

'''
   Both DFS or BFS can be used
'''
from collections import defaultdict

class Graph(object):
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def is_reachable_dfs(self, src, dest):
        visited = [False] * self.V

        queue = []
        queue.append(src)

        while len(queue) > 0:
            u = queue.pop(0)
            for i in self.graph[u]:
                if visited[i] == False:
                    if i == dest:
                        return True
                    queue.append(i)
                    visited[i] = True
        return False


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print g.is_reachable_dfs(1, 3)
print g.is_reachable_dfs(3, 1)