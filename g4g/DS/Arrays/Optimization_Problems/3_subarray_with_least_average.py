'''
   Find the subarray with least average
   Given an array arr[] of size n and integer k such that k <= n.

   Input:  arr[] = {3, 7, 90, 20, 10, 50, 40}, k = 3
    Output: Subarray between indexes 3 and 5
    The subarray {20, 10, 50} has the least average 
    among all subarrays of size 3.

    Input:  arr[] = {3, 7, 5, 20, -10, 0, 12}, k = 2
    Output: Subarray between [4, 5] has minimum average
'''

# SLIDING WINDOW TECHNIQUE
import sys

def leastAverage(arr, k):
    n = len(arr)
    cur_sum = 0
    for i in range(k):
        cur_sum += arr[i]
    index = 0
    min_sum = cur_sum
    for i in range(k, n):
        cur_sum = cur_sum + arr[i] - arr[i-k]
        if cur_sum < min_sum:
            min_sum = cur_sum
            index = i - k + 1
    
    return index, index+k

print leastAverage([3, 7, 90, 20, 10, 50, 40], 3)



