''' Detect a cycle in a directed graph '''

'''
   To detect a back edge, we can keep track of vertices currently in recursion
   stack of function for DFS traversal. If we reach a vertex that is already in
   the recursion stack, then there is a cycle in the tree. The edge that connects
   current vertex to the vertex in the recursion stack is a back edge. We have
   used recStack[] array to keep track of vertices in the recursion stack.
'''
from collections import defaultdict

class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for i in self.graph:
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, recStack) == True:
                    return True
        return False

    def isCyclicUtil(self, src, visited, recStack):
        # Mark current node as visited and
        # add to recursion stack
        visited[src] = True
        recStack[src] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for i in self.graph[src]:
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, recStack) == True:
                    return True
            elif recStack[i] == True:
                return True
        
        # Pop the node from recursion stack after it returns.
        recStack[src] = False
        return False


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print g.isCyclic()
