''' Count all possible nodes between 2 vertices '''

'''
   The problem can be solved using backtracking.
   i.e. We take a path and start walking it, if it
   leads to the destination then we count that path and
   backtrack to take another one. If the path does not
   lead us to the destination vertex, we discard the path.
'''

class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(self.V)]

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def count_path(self, src, dest):
        visited = [False] * self.V
        count = [0]
        self.count_path_util(visited, count, src, dest)
        return count[0]

    def count_path_util(self, visited, count, src, dest):
        visited[src] = True
        
        if src == dest:
            count[0] += 1
        else:
            i = 0
            while i < len(self.graph[src]):
                if visited[self.graph[src][i]] == False:
                    self.count_path_util(visited, count, self.graph[src][i], dest)
                i += 1
        visited[src] = False


g = Graph(4)  
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 0)
g.add_edge(2, 1)
g.add_edge(1, 3)

src = 2
dest = 3
print g.count_path(src, dest)
