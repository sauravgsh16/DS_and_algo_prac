'''
   Largest Sum Contiguous Subarray
'''
# Kadane's algorithm

def maxSum(arr):
    n = len(arr)

    max_so_far = 0
    max_ending_here = 0

    for i in range(n):
        max_ending_here += arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        
        if max_ending_here < 0:
            max_ending_here = 0
    
    return max_so_far




print maxSum([-2, -3, 4, -1, -2, 1, 5, -3])

