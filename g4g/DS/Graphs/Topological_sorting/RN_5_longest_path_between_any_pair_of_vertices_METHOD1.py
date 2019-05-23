''' Longest path between any pair of vertices '''

'''
   We are given a map of cities connected with each other via cable lines
   such that there is no cycle between any two cities. We need to find the
   maximum length of cable between any two cities for given city map.
'''

'''
   Solution:
   We create an undirected graph for given city map and preform DFS for every
   city to find maximum length of cable.
   While traversing, we look for the total cable length to reach the current city
   and if it's adjacent city is not visited, we call DFS for it. If all the
   adjacent cities are visited for current node, we update the max_length 
   accordingly.
'''

def DFS(graph, src, prev_len, max_len, visited):
    visited[src] = True

    curr_len = 0

    adjacent = None
  
    # Traverse all adjacent  
    for i in range(len(graph[src])): 
          
        # Adjacent element  
        adjacent = graph[src][i]
  
        # If node or city is not visited  
        if (not visited[adjacent[0]]): 
              
            # Total length of cable from 
            # src city to its adjacent  
            curr_len = prev_len + adjacent[1]  
  
            # Call DFS for adjacent city  
            DFS(graph, adjacent[0], curr_len,  
                            max_len, visited) 
  
        # If total cable length till  
        # now greater than previous  
        # length then update it  
        if (max_len[0] < curr_len):  
            max_len[0] = curr_len  
  
        # make curr_len = 0 for next adjacent  
        curr_len = 0

def longestCable(graph, n): 
      
    # maximum length of cable among 
    # the connected cities  
    max_len = [-999999999999]  
  
    # call DFS for each city to find  
    # maximum length of cable 
    for i in range(1, n + 1): 
          
        # initialize visited array with 0  
        visited = [False] * (n + 1)  
  
        # Call DFS for src vertex i  
        DFS(graph, i, 0, max_len, visited) 
  
    return max_len[0]


n = 6
  
graph = [[] for i in range(n + 1)] 

# create undirected graph  
# first edge  
graph[1].append([2, 3])  
graph[2].append([1, 3])  

# second edge  
graph[2].append([3, 4])  
graph[3].append([2, 4])  

# third edge  
graph[2].append([6, 2])  
graph[6].append([2, 2])  

# fourth edge  
graph[4].append([6, 6])  
graph[6].append([4, 6])  

# fifth edge  
graph[5].append([6, 5])  
graph[6].append([5, 5])  

print longestCable(graph, n)