''' Check if given graph is a tree '''


'''
   We can either use BFS or DFS to detect two properties

   1) Detect that there are no cycles. For every visited vertex 'v', if there is
   an adjacent vertex 'u', such that 'u' is already visited and 'u' is not a
   parent of 'v', then a cycle exists.

   2) Since graph is unidirected, we can start PFS or DFS from any vertex and
   check if all the vertices are reachable or not.
'''

from collections import defaultdict

class Graph(object):
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = defaultdict(list)

    def add_edge(self, v, u):
        self.graph[v].append(u)
        self.graph[u].append(v)

    # A recursive function that uses visited[]
    # and parent to detect cycle in subgraph
    # reachable from vertex v.
    def is_cycle_util(self, v, visited, parent):
        # Mark current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent for this vertex
        for i in self.graph[v]:

            # If an adjacent is not visited, then recur for that adjacent
            if visited[i] == False:
                if self.is_cycle_util(i, visited, v) == True:
                    return True
            # If an adjacent is visited and not
            # parent of current vertex, then there
            # is a cycle.
            elif i != parent:
                return True
        return False

    # Returns true if the graph is a tree, else false.
    def is_tree(self):
        # Mark all the vertices as not visited and not part of recursion stack
        visited = [False] * self.vertex

        # The call to is_cycle_util serves multiple  
        # purposes. It returns true if graph reachable  
        # from vertex 0 is cyclcic. It also marks  
        # all vertices reachable from 0.
        if self.is_cycle_util(0, visited, -1) == True:
            return False
        
        # If we find a vertex which is not reachable
        # from 0 (not marked by is_cycle_util(),
        # then we return false
        for i in range(self.vertex):
            if visited[i] == False:
                return False
        
        return True

g1 = Graph(5) 
g1.add_edge(1, 0) 
g1.add_edge(0, 2) 
g1.add_edge(0, 3) 
g1.add_edge(3, 4) 

print g1.is_tree()

g2 = Graph(5)
g2.add_edge(1, 0)
g2.add_edge(0, 2)
g2.add_edge(2, 1)
g2.add_edge(0, 3)
g2.add_edge(3, 4)

print g2.is_tree()