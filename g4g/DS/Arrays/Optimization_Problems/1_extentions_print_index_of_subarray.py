'''
   Largest Sum Contiguous Subarray

   Print indexes of the start and end of the subarray too
'''
import sys

def maxSum(arr):
    n = len(arr)

    max_so_far = -sys.maxsize
    max_ending_here = 0

    start = 0
    end = 0
    s = 0

    for i in range(n):
        max_ending_here += arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1
    return max_so_far, start, end

print maxSum([-2, -3, 4, -1, -2, 1, 5, -3])