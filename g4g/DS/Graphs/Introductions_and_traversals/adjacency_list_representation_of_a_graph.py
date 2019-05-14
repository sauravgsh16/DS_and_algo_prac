''' Adjacency list representation of a graph '''


class AdjNode(object):
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None


class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * vertices

    def add_edge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding source to destination, as it is an undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.vertices):
            print 'Adjacency list of vertex {} \n head'.format(i)
            temp = self.graph[i]
            while temp:
                print ' --> {}'.format(temp.vertex),
                temp = temp.next
            print '\n'


V = 5
graph = Graph(V)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.print_graph()
