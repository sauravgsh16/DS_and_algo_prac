''' Floyd Warshall Algorithm based solution '''

'''
   Distance of any node from itself is always Zero.
   But in some case, as in this example, when we traverse from 4 to 1, the
   distance come out to be -2, i.e distance distance from 1 to 1 will become -2.
   This is our catch, we just have to check the nodes distance from itself and
   if it comes out to be negative, we will detect the required negative cycle.
'''

V = 4
INF = 99999

def detect_negative_using_floyd_warshall(graph):

    # Output matrix
    dist = map(lambda i: map(lambda j: j, i), graph)

    # Update output matrix using floyd-warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], (dist[i][k] + dist[k][j]))

    # Check distance of any node from itself.
    # If distance is negative, then negative cycle exists

    for i in range(V):
        for j in range(V):
            if dist[i][j] < 0:
                return True
    return False

def print_solution(dist):
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print '%7s' % ("INF"),
            else:
                print '%7d\t' % dist[i][j],
            if j == V - 1:
                print ""

graph = [[0, 1, INF, INF],
         [INF, 0, -1, INF],
         [INF, INF, 0, -1],
         [-1, INF, INF, 0]]

print detect_negative_using_floyd_warshall(graph)
