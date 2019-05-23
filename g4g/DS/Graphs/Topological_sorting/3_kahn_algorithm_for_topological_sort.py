''' Kahn's algorithm for topological sort in a Directed Acyclic Graph '''

'''
   A DAG contains atleast one vertex with in-degree = 0 and one vertex with
   out-degree = 0
   Algorithm:
    1) Compute in-degree of each vertex.
    2) Pick all vertex with in-degree = 0 and add them into a queue.
    3) Remove a vertex from the queue and then
        a) Increment count of visited nodes by 1
        b) Decrease in-degree by 1 for all it's neighboring nodes.
        c) If in-degree of a neighboring nodes is reduced to zero, then add it
           to the queue.
    4) Repeat 3 until queue is empty
    5) If count of visited nodes is not equal to number of node in the graph
       then topological sort is not possible for the given graph
'''

from collections import defaultdict

class Graph(object):
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.indegree = [0] * V

    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        self.indegree[dest] += 1

    def topological_sort(self):
        # We already have created the in-degree array.
        # Alt method:
        '''
        in_degree = [0] * self.V

        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1
        '''
        # Define a queue
        queue = []
        # vector to store result of topological sort
        result = []
        # Initialize count of visited nodes:
        count = 0

        # Enqueue all vertex with in-degree 0
        for i in range(self.V):
            if self.indegree[i] == 0:
                queue.append(i)

        while len(queue) > 0:

            u = queue.pop(0)
            result.append(u)

            for i in self.graph[u]:
                self.indegree[i] -= 1
                # If in-degree becomes zero, add it to the queue
                if self.indegree[i] == 0:
                    queue.append(i)
            count += 1

        if count != self.V:
            print "There exists a cycle in the graph"
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
print g.graph