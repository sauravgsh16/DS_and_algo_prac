''' Check if graph has cycles of odd lenght '''

'''
   A graph does not contain cycles of odd lenght if and only if it is Bipartite,
   i.e it can be coloured with two colors.
   It is obvious that if a graph has an odd length cycle then it cannot be Bipartite.
   In Bipartite graph there are two sets of vertices such that no vertex in a
   set is connected with any other vertex of the same set. For a cycle of odd length,
   two vertices must of the same set be connected which contradicts Bipartite definition.
'''

'''
   Solution: Basically check if graph is Bipartite. To check if a graph is
   Bipartite, we can check if the graph can be colored using 2 colors
'''

def check_graph_contains_odd_cycles(graph, src):

    '''
    Create a color array to store colors assigned to all vertices.
    Vertex number is used as index in this array. The value '-1' indicates that
    no color is assigned to vertex. The value '1' indicates first color and the
    value '0' indicates second color.
    '''
    colorArr = [-1] * V

    # Assigning first color to source
    colorArr[src] = 1

    q = []
    q.append(src)

    while len(q) > 0:

        u = q.pop(0)

        # Return true if there is a self-loop
        if graph[u][u] == 1:
            return True
        
        for v in range(V):

            # An edge from u to v exists and destination 'v' is not coloured.
            if graph[u][v] and colorArr[v] == -1:

                # Assign alternate color to this adjacent v of u
                colorArr[v] = 1 - colorArr[u]
                q.append(v)
            # An edge from u to v exists and destination 'v' is colored with
            # same color as u
            elif graph[u][v] and colorArr[v] == colorArr[u]:
                return True
    
    # If we reach here, then all adjacent vertices can be colored with 2 colors.
    return False

V = 4
graph = [[0, 1, 0, 1],
         [1, 0, 1, 0],
         [0, 1, 0, 1],
         [1, 0, 1, 0]]

print check_graph_contains_odd_cycles(graph, 0)
