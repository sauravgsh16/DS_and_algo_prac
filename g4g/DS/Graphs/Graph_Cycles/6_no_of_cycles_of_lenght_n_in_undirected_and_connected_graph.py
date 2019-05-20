''' Number of cycles of lenght N in an undirected and connected graph '''


'''
   Idea is to perform DFS.
   Using DFS we find every possible path of length (n-1) for a particular source.
   Then we check if this path ends with the vertex it started with, if yes then
   we count this as the cycle of length n.
   Notice that we looked for path of lenght (n-1) because the nth edge will be
   the closing edge of the cycle.

   Every possible path of lenght (n-1) can be searched using only V-(n-1) vertices.
   For eg, all the cycles of lenght 4 can be searched using only 5-(4-1) = 2 vertices.
   The reason behind this is because, we search all possible path of length (n-1) = 3
   using these 2 vertices which include the remaining 3 vertices. So, these 2
   vertices cover the cycles of remaining 3 vertices as well, and using only
   3 vertices we can't form a cycle of length 4 anyway.

   One more thing is to notice is that, every vertex finds 2 duplicate cycles, for
   every cycle that it forms. For eg: 0th vertex finds two duplicate cycles namely:
   0 -> 3 -> 2 -> 1 -> 0 and 0 -> 1 -> 2 -> 3 -> 0. Hence the total count must be
   divided by 2 because every cycle is counted twice.
'''

V = 5

def dfs(graph, marked, n, vertex, start, count):
    # mark the vertex as visited.
    marked[vertex] = True

    # if the path of lenght (n-1) is found
    if n == 0:

        # mark vertex as un-visited to make it usable again
        marked[vertex] = False

        # Check if vertex can end with start
        if graph[vertex][start] == 1:
            count += 1
            return count
        else:
            return count
    
    # For searching every possinle path of lenght (n-1)
    for i in range(V):
        if marked[i] == False and graph[vertex][i] == 1:

            # DFS for searching path by descreasing the length by 1
            count = dfs(graph, marked, n-1, i, start, count)
    
    # Mark vertex as unvisited to make it reusable.
    marked[vertex] = False
    return count


def count_cycles(graph, n):

    marked = [False] * V

    count = 0
    for i in range(V-(n-1)):
        count = dfs(graph, marked, n-1, i, i, count)
        
        # mark vertex 'i' as visited and it will not be visited again.
        marked[i] = True
    
    return count/2


graph = [[0, 1, 0, 1, 0],
         [1 ,0 ,1 ,0, 1],
         [0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0]]
n = 4
print 'Total cycles of lenght {} are {}'.format(n, count_cycles(graph, n))
