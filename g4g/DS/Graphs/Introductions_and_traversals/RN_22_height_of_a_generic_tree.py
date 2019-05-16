''' Height of a generic tree '''

'''
   Problem Statement:
    We are given a tree of size n as array parent[0..n-1] where every index i
    in parent[] represents a node and the value at i represents the immediate
    parent of that node. For root node value will be -1. Find the height of the
    generic tree given the parent links.

    Input : parent[] = {-1, 0, 0, 0, 3, 1, 1, 2}
    Output : 2

    Input  : parent[] = {-1, 0, 1, 2, 3}
    Output : 4
'''

# Method 1:
# We traverse up the tree from node to root. while traversing we keep track
# of the maximum reached level.
# Time - O(n^2)

# Method 2:
# We create a tree in O(n) time. Then preform BFS, while maintaining the max
# level. Requires 2 traversals of the tree

from collections import defaultdict

def build_tree(arr, adj):
    root_idx = 0
    for i in range(len(arr)):
        if arr[i] == -1:
            root_idx = i
        else:
            adj[i].append(arr[i])
            adj[arr[i]].append(i)
    return root_idx


def BFS(root, adj, arr):
    visited = [False] * len(arr)
    queue = []
    queue.append(root)
    visited[root] = True
    heights = [0] * len(arr)

    while len(queue) > 0:
        s = queue.pop(0)
        for i in adj[s]:
            if not visited[i]:
                heights[i] = heights[s] + 1
                visited[i] = True
                queue.append(i)
    return reduce(lambda x, y: max(x, y), heights)


def tree_height(arr):
    adj = defaultdict(list)
    root = build_tree(arr, adj)
    return BFS(root, adj, arr)

arr1 = [-1, 0, 0, 0, 3, 1, 1, 2]
arr2 = [-1, 0, 1, 2, 3]
print tree_height(arr1)
print tree_height(arr2)

# Method 3
# We use recursion to return height of a particular node.
# O(n), but requires only one iteration

def tree_height_recursion(arr):
    max_height = 0
    visited = [False] * len(arr)
    height = [0] * len(arr)
    for i in range(len(arr)):
        if not visited[i]:
            height[i] = tree_height_recur_util(arr, i, visited, height)
            max_height = max(max_height, height[i])
    return max_height

def tree_height_recur_util(arr, node, visited, height):
    if arr[node] == -1:
        if not visited[node]:
            visited[node] = True
            return 0
    
    if visited[node] == True:
        return height[node]
    
    height[node] = 1 + tree_height_recur_util(arr, arr[node], visited, height)
    return height[node]

arr1 = [-1, 0, 0, 0, 3, 1, 1, 2]
arr2 = [-1, 0, 1, 2, 3]
print tree_height_recursion(arr1)
print tree_height_recursion(arr2)