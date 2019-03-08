'''
   Minimum number of jumps to reach end

   Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
   Output: 3 (1-> 3 -> 8 ->9)
'''
# DYNAMIC PROGRAMMING IMPLEMENTATION
'''
   Method 2 (Dynamic Programming) 
   In this method, we build a jumps[] array from left to right such that jumps[i] 
   indicates the minimum number of jumps needed to reach arr[i] from arr[0]. 
   Finally, we return jumps[n-1].
'''
# TIME COMPLEXITY - O(n^2)

import sys

def minJumps(arr):
    n = len(arr)
    jumps = [sys.maxsize] * n

    if n == 0 or arr[0] == 0:
        return -1
    jumps[0] = 0

    for i in range(1, n):
        for j in range(i):
            if (i <= arr[j] + j) and jumps[j] != sys.maxsize:
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n-1]


print minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9])