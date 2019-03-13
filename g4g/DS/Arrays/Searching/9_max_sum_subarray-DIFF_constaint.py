'''
   Maximum Subarray Sum Excluding Certain Elements
   Given an array of A of n integers and an array B of
   m integers find the Maximum Contiguous Subarray 
   Sum of array A such that any element of array B is not present in that subarray

   Examples :

   Input : A = {1, 7, -10, 6, 2}, B = {5, 6, 7, 1}
   Output : 2
   Explanation Since the Maximum Sum Subarray of A is not allowed to have
   any element that is present in array B.
   The Maximum Sum Subarray satisfying this is {2} as the only allowed subarrays are:
   {-10} and {2}. The Maximum Sum Subarray being {2} which sums to 2
'''

# We apply kadane's alorigthms with a little twist, since we want to avoid all elements
# present in array B.
import sys

def maxSum(arr_a, arr_b):
    n = len(arr_a)
    max_so_far = -sys.maxsize
    max_ending_here = 0

    for i in range(n):
        # Check if element is present in array B,
        # we reset the max count
        if arr_a[i] in arr_b: # ALGORITHM improve point (Can be linear or binary)
            max_ending_here = 0
            continue
        
        max_ending_here += arr_a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

print maxSum([1, 7, -10, 6, 2], [5, 6, 7, 1])
            