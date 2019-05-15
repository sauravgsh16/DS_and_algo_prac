''' Transpose of a graph '''

# Below we find the transpose of a graph represented as an adjacency list
# If a graph is represented as an adjacency matrix, we just find the transpose of
# that matrix

class Graph(object):
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(self.V)]

    def add_edge(self, src, dest):
        self.adj[src].append(dest)


def get_transpose(V, g):
    t = Graph(V)
    for i in range(V):
        for j in range(len(g.adj[i])):
            t.add_edge(g.adj[i][j], i)
    return t

def display_graph(V, g):
    for i in range(V):
        print '{} -->'.format(i),
        for j in range(len(g.adj[i])):
            print g.adj[i][j],
        print


V = 5
g = Graph(V)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(0, 3)
g.add_edge(2, 0)
g.add_edge(3, 2)
g.add_edge(4, 1)
g.add_edge(4, 3)

transpose = get_transpose(V, g)
print 'Printing Graph'
display_graph(V, g)
print 'Printing Transpose'
display_graph(V, transpose)
