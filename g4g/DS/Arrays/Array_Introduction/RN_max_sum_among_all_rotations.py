# -*- coding: utf-8 -*-
'''
   Maximum sum of i*arr[i] among all rotations of a given array
   Maximum that maximizes sum of value of i*arr[i] where i varies from 0 to n-1.
'''

# Naive approach
# Complexity -O(n^2)
import sys
import unittest

def maxSumNaive(arr):
    n = len(arr)
    res = -sys.maxsize

    for i in range(n):
        # Initialize sum of current rotation
        cur_sum = 0
        # We don't actually rotate the array
        # but compute sum by finding the indexes when
        # arr[i] is the first element
        for j in range(n):
            index = int((i + j) % n)
            cur_sum += j * arr[index]
        
        res = max(res, cur_sum)
    return res


'''
Optimized algorithm

The idea is to compute value of a rotation using value of previous rotation.
When we rotate an array by one, following changes happen in sum of i*arr[i].
1) Multiplier of arr[i-1] changes from 0 to n-1: i.e. arr[i-1] * (n-1) is added to current value.
2) Multipliers of other terms is decremented by 1: i.e. (cum_sum – arr[i-1]) is 
   subtracted from current value where cum_sum is sum of all numbers.
'''

def maxSumOptimized(arr):
    n = len(arr)
    
    # Compute sum of all array elements
    cum_sum = 0
    for i in range(n):
        cum_sum += arr[i]
    
    # Compute sum of i * arr[i] for initial comfig
    curr_val = 0
    for i in range(n):
        curr_val += i * arr[i]

    res = curr_val
    for i in range(1, n):
        # Compute next value using previous 
        # value in O(1) time 
        next_val = (curr_val - (cum_sum - arr[i-1]) + arr[i-1] * (n-1))
        # Update current value 
        curr_val = next_val
        # Update result if required 
        res = max(res, next_val)

    return res

class TestMaxSum(unittest.TestCase):
    ARRAY1 = [1, 20, 2, 10]
    ARRAY2 = [8, 3, 1, 2]

    def test1_naive(self):
        op = 72
        res = maxSumNaive(self.ARRAY1)
        self.assertEqual(op, res)

    def test2_optimized(self):
        op = 29
        res = maxSumOptimized(self.ARRAY2)
        self.assertEqual(op, res)

if __name__ == '__main__':
    unittest.main()
