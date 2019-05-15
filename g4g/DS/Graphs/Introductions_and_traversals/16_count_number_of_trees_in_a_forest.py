''' Count number of trees in a forest '''

'''
   If we preform DFS for all nodes in the graph, in case there are more than
   1 tree, i.e. it will be a disconnected graph.
   In that case the number of times we perform DFS will be the no of trees. 
'''
from collections import defaultdict

class Graph(object):
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)


    def DFS_util(self, visited, s):
        visited[s] = True

        for i in self.graph[s]:
            if visited[i] == False:
                self.DFS_util(visited, i)

    def count_trees_dfs(self):
        visited = [False] * self.V
        count = 0
        for i in range(self.V):
            if visited[i] == False:
                count += 1
                self.DFS_util(visited, i)
        return count

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(3, 4)

print g.count_trees_dfs()