### Graph and it's representations

Graph consists of following 2 components:
    1) A finite set of `vertices`
    2) A finite set of ordered pair of the form (u, v) called as `edge`.
       The pair is ordered as, (u, v) is not the same as (v, u) in case of 
       a `directed graph`. (u, v) indicates an edge from vertex u to vertex v.
       An edge may contain `weight/value/cost`.

The following as the most commonly used representationso of a graph.
1) Adjacency Matrix
2) Adjacency List

### Adjacency Matrix
Adjacency Matrix is a 2D array of size V x V, where V is the number of vertices.
Representation:
```py
    [[0, 1, 0],
     [1, 0, 1],
     [0, 1, 0]]
```
1 denotes an edge from one vertex to another.
Adjacency matrix for an `undirected graph` is always `symmetric`
Adjacency matrix can also be used to represent `weighted graph`

Pros:
    1) Representation is easier to implement and follow.
    2) Removing an edge takes O(1) time.
    3) Queries of edges between 'u' and 'v' is also O(1) time.

Cons:
    1) Consumes more space O(n^2).
    2) Adding a vertex is O(n^2) operation.

```py

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
        self.adjMatrix[dest][orig] = cost # Do not add for directed graph

    def get_vertex(self):
        return self.verticesList

    def get_edges(self):
        edges = []
        for i in range(self.numVertex):
            for j in range(self.numVertex):
                if self.adjMatrix[i][j] != -1:
                    edges.append(self.verticesList[i], self.verticesList[j],
                        self.adjMatrix[i][j])
        return edges

    def get_matrix(self):
        return self.adjMatrix
```

### Adjacency List

An array is used. Size of the array is equal to the number of vertices.
Let `arr` be an array. An entry `arr[i]` represents the list of vertices
adjacent to the ith vertex.
This representation can alos be used to represent a weighted graph.
The weights of edges can be represented as lists of pairs.
Following is adjacency list representation of the below graph


```
 0---1
 |  /| \ 2
 | / | /
 4---3

0 --> 1 --> 4
1 --> 0 --> 4 --> 3 --> 2
2 --> 1 --> 3
3 --> 1 --> 4 --> 2
4 --> 3 --> 0 --> 1
```

```py

''' Implementation of a graph using a adjacency list '''

class AdjNode(object):
    def __init__(self, val):
        self.vertex = val
        self.next = None


class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices

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
            print 'Adjacency list of vertex {} \n head.'.format(i)
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
```