''' Check loop in array according to given constraints '''

'''
   Given an array arr[0..n-1] of positive and negative numbers we need to find
   if there is a cycle in array with given rules of movements. If a number at
   an i index is positive, then move arr[i]%n forward steps,
   i.e. next index to visit is (i + arr[i])%n. Conversely, if it's negative,

   Here n is size of array. If value of arr[i]%n is zero, then it means no move from index i.

   Eg:

    Input: arr[] = {2, -1, 1, 2, 2}
    Output: Yes
    Explanation: There is a loop in this array
    because 0 moves to 2, 2 moves to 3, and 3 
    moves to 0.

    Input  : arr[] = {1, 1, 1, 1, 1, 1}
    Output : Yes
    Whole array forms a loop.

    Input  : arr[] = {1, 2}
    Output : No
    We move from 0 to index 1. From index
    1, there is no move as 2 % n is 0. Note that
'''

'''
   The Idea is to form a directed graph of array elements using given set of
   rules. While forming graph we don't make self loops.
   The we just check if there are cycles present in a directed graph.
'''

def create_graph(arr, n):
    adj_list = [[] for _ in range(n)]

    for i in range(n):
        if i != (i + arr[i]) % n:
            adj_list[i].append((i + arr[i]) % n)
    return adj_list


def dfs_loop_detect(adj_list, src, visited, recur_stack):
    visited[src] = True
    recur_stack[src] = True

    for i in adj_list[src]:
        if visited[i] == False:
            if dfs_loop_detect(adj_list, i, visited, recur_stack) == True:
                return True
        elif recur_stack[i] == True:
            return True
    recur_stack[src] = False
    return False


def detect_loops(arr):
    n = len(arr)
    adj_list = create_graph(arr, n)
    visited = [False] * n
    recur_stack = [False] * n

    for i in range(n):
        if visited[i] == False:
            if dfs_loop_detect(adj_list, i, visited, recur_stack):
                return True
    return False


arr1 = [2, -1, 1, 2, 2]
arr2 = [1, 2]
print detect_loops(arr1)
print detect_loops(arr2)
