''' Clone a directed Acyclic Graph in O(1) space '''

from collections import defaultdict

class Graph(object):
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)


def clone_util_using_dfs(clone, g, src, visited):
    for i in g.graph[src]:
        if visited[i] == False or i not in clone.graph[src]:
            clone.add_edge(src, i)
            clone_util_using_dfs(clone, g, i, visited)
    visited[src] = True


def clone_graph(g):
    clone = Graph(g.V)
    visited = [False] * g.V
    for i in range(g.V):
        if visited[i] == False:
            clone_util_using_dfs(clone, g, i, visited)
    return clone


def dfs_util(g, src, visited):
    visited[src] = True
    print src,

    for i in g.graph[src]:
        if visited[i] == False:
            dfs_util(g, i, visited)  

def dfs(g):
    visited = [False] * g.V
    for i in range(g.V):
        if visited[i] == False:
            dfs_util(g, i, visited)
    print


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

clone = clone_graph(g)
dfs(g)
dfs(clone)


