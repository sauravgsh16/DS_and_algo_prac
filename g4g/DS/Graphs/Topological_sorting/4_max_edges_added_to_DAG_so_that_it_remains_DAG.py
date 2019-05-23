''' Maximum number of edges that can be added to a DAG so that it ramains a DAG '''

'''
   The trick is to perform a topological sort.
   Then add edges from left to right nodes if they are not present already.
'''
from collections import defaultdict

class Graph(object):
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def get_topological_sort(self):
        indegree = [0] * self.V

        for i in range(self.V):
            for j in self.graph[i]:
                indegree[j] += 1
        
        queue = []
        for i in range(self.V):
            if indegree[i] == 0:
                queue.append(i)

        topological = []
        while len(queue) > 0:
            u = queue.pop(0)
            topological.append(u)

            for i in self.graph[u]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        return topological

    def max_edges(self):
        topo = self.get_topological_sort()
        edges = [0] * self.V

        for i in range(len(topo)):
            for j in range(i+1, len(topo)):
                if topo[j] not in self.graph[topo[i]]:
                    edges[topo[i]] += 1
        
        print edges
        


g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

g.max_edges()