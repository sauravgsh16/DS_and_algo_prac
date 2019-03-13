'''
   Find the Minimum length Unsorted Subarray, sorting which makes the complete array sorted

   Input:  [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
   Output: subarray between indexes 3 and 8
'''
import sys

def minLenght(arr):
    n = len(arr)
    min_l = False
    min_r = False
    l = 0
    r = n - 1
    while not (min_l and min_r) and (l < r):
        if not min_l:
            if arr[l] > arr[l+1]:
                min_l = True
            else:
                l += 1
        if not min_r:
            if not min_r:
                if arr[r] < arr[r-1]:
                    min_r = True
                else:
                    r -= 1
    maxElement = l
    for i in range(l+1, r+1):
        if arr[i] > arr[maxElement]:
            maxElement = i
    i = n-1
    min_v = sys.maxsize
    index = n - 1
    while i > r:
        curr_val = arr[maxElement] - arr[i]
        if curr_val > 0 and curr_val < min_v:
            min_v = curr_val
            index = i
        i -= 1

    return l, index

print minLenght([0, 1, 15, 25, 6, 7, 30, 40, 50])