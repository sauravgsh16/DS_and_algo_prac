'''
   Find subarray with given sum | Set 1 (Nonnegative Numbers)
   Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number.

   Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
   Ouptut: Sum found between indexes 2 and 4

   Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
   Ouptut: Sum found between indexes 1 and 4
'''

def findSubArray(arr, s):
    n = len(arr)
    cur_sum = 0
    start = last = 0

    while cur_sum != s and last <= n-1:
        if cur_sum < s:
            cur_sum += arr[last]
            last += 1
        elif cur_sum > s:
            cur_sum -= arr[start]
            start += 1
    
    if cur_sum == s:
        return start, last-1
    else:
        return 0

print findSubArray([1, 4, 20, 3, 10, 5], 33)