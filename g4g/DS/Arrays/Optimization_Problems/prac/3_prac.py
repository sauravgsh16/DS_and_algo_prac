'''
   Subarray with least sum
'''

def minSumSubarray(arr, k):
    n = len(arr)

    cur_sum = 0
    for i in range(k):
        cur_sum += arr[i]
    min_sum = cur_sum
    index = 0
    for i in range(k+1, n):
        cur_sum += arr[i] - arr[i-k]
        if cur_sum < min_sum:
            min_sum = cur_sum
            index = i - k + 1
    
    return index, index + k

print minSumSubarray([3, 7, 90, 20, 10, 50, 40], 3)