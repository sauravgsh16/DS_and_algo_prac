''' Find mother vertex in a Graph '''

'''
   A mother vertex 'v', is a vertex such that all other vertex in the graph can
   be reached by a path from V.

   How to find a mother vertex:

   Case1: Undirected Connected Graph: In this case, all the vertices are mother
   vertices as we can reach to all the other nodes in the graph

   Case2: Undirected/Directed Disconnected Graph: In this case, there is no
   mother vertex as we cannot reach to all the other nodes in the graph

   Case3: Directed Connected Graph: In this case, we have to find a vertex 'v',
   such that, we can reach all the other nodes through a directed path.


   A Naive approach:
   Perform DFS/BFS on all the vertices and find whether we can reach all the
   vertices from the vertex. This approach takes O(V*(E+V)) time, which is
   very inefficient for large graphs.

   Efficient approach:
   Based on "Kosaraju's Strongly Connected Component Algorithm"
   In a graph of strongly connected components, mother vertices are always
   vertices of source component in component graph.

   ****The idea is based on below fact:****
   If there exists, a mother vertex (or vertices), then one of the mother vertices
   is the last finished vertex in DFS. (or a mother vertex has the maximum
   finish time in DFS traversal)

   A vertex is said to be finished in DFS is a recursive call for its DFS is over,
   i.e. all descendants of the vertex have been visited.

   HOW DOES THE ABOVE IDEA WORK? **
   Let the last finished vertex be v. Basically we need to prove that there
   cannot be another vertex 'u' to v, if u is not another mother vertex. (or
   there cannot exist a non-mother vertex u such that, u --> is an edge.). There
   can be two possibilities.
   1) Recursive DFS call is made for u before v. If an edge u --> v exists, then
      v must have finished before u because v is reachable through u and a vertex
      finished after all its decendants
   2) Recursive DFS call is made for v before u. Tf an edge u --> v exists, then
      either v must finish before u, (which contradicts our assumption that v
      is finished at the end) OR u should be reachable from v (which means u is
      another mother vertex).

   ALGORITHM **
   1) Do DFS traversal of the given graph. While doing traversal keep track of
      last finished vertex 'v'. This step takes O(V + E) time.
   2) If there exists mother vertex (or vertices), then v must be one(or one of
      them). Check if v is a mother vertex by doing DFS/BFS from v. This step
      also takes O(V+E) time.
'''
from collections import defaultdict

class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def DFS_util(self, v, visited):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS_util(i, visited)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def find_mother(self):
        visited = [False] * self.vertices

        # To store the finished vertex
        v = 0

        # DFS to find last finished vertex
        for i in range(self.vertices):
            if visited[i] == False:
                self.DFS_util(i, visited)
                v = i
        
        # If there exists a mother vertex (or vertices) in give graph,
        # then v must be one (or one of them)

        # Reset visited and perform DFS again, with v as starting point
        visited = [False] * self.vertices
        self.DFS_util(v, visited)
        if any(i == False for i in visited):
            return -1
        return v


g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(4, 1)
g.add_edge(6, 4)
g.add_edge(5, 6)
g.add_edge(5, 2)
g.add_edge(6, 0)

print 'A mother vertex is {}'.format(str(g.find_mother()))