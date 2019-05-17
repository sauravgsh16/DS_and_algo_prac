''' Detect a negative cycle in a graph '''

'''
   We use Bellman-Ford's algorithm to solve this problem.
   This idea, is that after preforming all 'Relaxations' in Bellman-Ford, we should
   be able to find the shortest distance for a single source.

   We preform another relaxation, if we encounter a shorter path for any vertex,
   we know that there is a negative weight cycle.
'''
import sys
from collections import defaultdict


class Vertex(object):
    def __init__(self, idx):
        self.idx = idx
        self.weight = sys.maxsize

    def get_weight(self):
        return self.weight

    def set_weight(self, val):
        self.weight = val


class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, src, dest, edge_weight):
        self.graph.append((src, dest, edge_weight))


def bellman_ford_shorted_path(g, src):

    # Set initial source to 0
    src.weight = 0

    for _ in range(g.vertices - 1):
        for edge_tuple in g.graph:
            if edge_tuple[0].weight + edge_tuple[2] < edge_tuple[1].weight:
                edge_tuple[1].weight = edge_tuple[0].weight + edge_tuple[2]
    
    # Perform one more relaxation for all edges.
    # If any edges changes, return True for existence of a negative cycle
    for edge_tuple in g.graph:
        if edge_tuple[0].weight + edge_tuple[2] < edge_tuple[1].weight:
            return True
    return False

g = Graph(2)
v1 = Vertex(0)
v2 = Vertex(1)
v3 = Vertex(2)
v4 = Vertex(3)
g.add_edge(v1, v2, 1)
g.add_edge(v2, v3, -1)
g.add_edge(v3, v4, -1)
g.add_edge(v4, v1, -1)

print bellman_ford_shorted_path(g, v1)
