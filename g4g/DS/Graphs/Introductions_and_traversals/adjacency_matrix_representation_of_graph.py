''' Representing a graph as an adjacency matrix '''


class Graph(object):
    def __init__(self, numVertex):
        self.adjMatrix = [[-1] * numVertex for x in range(numVertex)]
        self.numVertex = numVertex
        self.vertices = {}
        self.verticesList = [0] * numVertex

    def set_vertex(self, vertex, v_id):
        if 0 <= vertex <= self.numVertex:
            self.vertices[v_id] = vertex
            self.verticesList[vertex] = v_id

    def set_edge(self, orig, dest, cost=0):
        orig = self.vertices[orig]
        dest = self.vertices[dest]
        self.adjMatrix[orig][dest] = cost
        self.adjMatrix[dest][orig] = cost  # Do not add for directed graph

    def get_vertex(self):
        return self.verticesList

    def get_edges(self):
        edges = []
        for i in range(self.numVertex):
            for j in range(self.numVertex):
                if self.adjMatrix[i][j] != -1:
                    edges.append((self.verticesList[i], self.verticesList[j],
                                  self.adjMatrix[i][j]))
        return edges

    def get_matrix(self):
        return self.adjMatrix


graph = Graph(6)
graph.set_vertex(0, 'a')
graph.set_vertex(1, 'b')
graph.set_vertex(2, 'c')
graph.set_vertex(3, 'd')
graph.set_vertex(4, 'e')
graph.set_vertex(5, 'f')
graph.set_edge('a', 'e', 10)
graph.set_edge('a', 'c', 20)
graph.set_edge('c', 'b', 30)
graph.set_edge('b', 'e', 40)
graph.set_edge('e', 'd', 50)
graph.set_edge('f', 'e', 60)
print "Vertices of Graph"
print graph.get_vertex()
print "Edges of Graph"
print graph.get_edges()
print"Adjacency Matrix of Graph"
print graph.get_matrix()
