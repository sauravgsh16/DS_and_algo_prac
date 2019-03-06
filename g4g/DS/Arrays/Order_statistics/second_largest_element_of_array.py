'''
   Second largest element of an array
'''
import sys

# O(n)
def secondLargest(arr):
    n = len(arr)
    first = -sys.maxsize
    second = -sys.maxsize

    for i in range(n):
        if arr[i] > first:
            second = first
            first = arr[i]
    
        elif arr[i] > second and arr[i] != first:
            second = arr[i]
    
    return second


arr = [12, 35, 1, 10, 34, 1]
print secondLargest(arr)