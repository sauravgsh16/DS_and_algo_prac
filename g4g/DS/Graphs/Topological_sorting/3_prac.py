''' Kahn's topological sort '''

from collections import defaultdict

class Graph(object):
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)


    def topological_sort(self):
        # create in-degree array
        in_degree = [0] * self.V
        for i in range(self.V):
            for j in self.graph[i]:
                in_degree[j] += 1
        
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)
        
        result = []
        count = 0
        while len(queue) > 0:
            u = queue.pop(0)
            result.append(u)

            for i in self.graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
            
            count += 1

        if count != self.V:
            print 'Graph contains cycle'
        else:
            print result


g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

g.topological_sort()