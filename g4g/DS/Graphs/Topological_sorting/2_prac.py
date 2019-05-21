''' All topological sort '''


from collections import defaultdict

class Graph(object):
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.indegree = [0] * self.V

    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        self.indegree[dest] += 1

    def topological_sort_all_util(self, visited, stack):
        flag = False

        for i in range(self.V):
            if visited[i] == False and self.indegree[i] == 0:
                visited[i] = True
                stack.append(i)

                for j in self.graph[i]:
                    self.indegree[j] -= 1
                
                self.topological_sort_all_util(visited, stack)

                for j in self.graph[i]:
                    self.indegree[j] += 1
                stack.pop()
                visited[i] = False

                flag = True
        
        if flag == False:
            for i in stack:
                print i,
            print

    def topological_sorts_all(self):
        visited = [False] * self.V
        stack = []
        self.topological_sort_all_util(visited, stack)

g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)


g.topological_sorts_all()
