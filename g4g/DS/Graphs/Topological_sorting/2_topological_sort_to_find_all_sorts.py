''' All topological sorts of a directed acyclic graph '''

'''
   In a Directed acyclic graph many a times we can have vertices which are unrelated
   to each other because of which we can order them in many ways. These various
   topological sorting is important in many cases, for example if some relative weight
   is also available between the vertices, which is to minimize then we need to take care
   of relative ordering as well as their relative weight, which creates the need of checking
   through all possible topological ordering.
'''

'''
   Algorithm:
   We use backtracking to find all possible ordering.
   1) Initialize all vertices as not visited.
   2) Now choose vertex which is unvisited and has zero indegree and decrease indegree of all
      those vertices by 1 (corresponding to removing edges) now add this vertex to result and call
      the recursive function again and backtrack.
   3) After returning from function reset values of visited, result and indegree for
      enumeration of other possibilities.
'''

from collections import defaultdict

class Graph(object):
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.indegree = [0] * self.V

    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        self.indegree[dest] += 1

    def all_topological_sorts_util(self, visited, stack):
        # To indicate all topological sorts are found or not
        flag = False

        for i in range(self.V):
            print "############################"
            print i
            if visited[i] == False and self.indegree[i] == 0:
                print "****************************"
                print self.indegree, i, self.graph[i]
                print "******"
                visited[i] = True
                # include in the result
                stack.append(i)
                for j in self.graph[i]:
                    self.indegree[j] -= 1
                print "******"
                print self.indegree, i, self.graph[i]
                print "****************************"
                print "Calling Recursion for ", i
                self.all_topological_sorts_util(visited, stack)


                # Reset visited, stack and indegree for backtracking
                print "Resetting for i ", i
                visited[i] = False
                stack.pop()
                for j in self.graph[i]:
                    self.indegree[j] += 1
                
                flag = True
        
        if flag == False:
            for i in stack:
                print i,
            print

    def all_topological_sorts(self):
        visited = [False] * self.V
        stack = []
        self.all_topological_sorts_util(visited, stack)
        

g = Graph(4)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)

g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

  
print g.indegree
g.all_topological_sorts()