'''
   Shortest Un-ordered Subarray
   An array is given of n length, and problem is that we have to
   find the length of shortest unordered {neither increasing nor decreasing}
   sub array in given array.

   Input : n = 5
        7 9 10 8 11
   Output : 3
   Explanation : 9 10 8 unordered sub array.

   Input : n = 5
       1 2 3 4 5
   Output : 0 
   Explanation :  Array is in increasing order.
'''

# Shortest unordered subarray can have a lenght of either 0 or 3

def increasing(arr):
    n = len(arr)

    for i in range(n-1):
        if arr[i] >= arr[i+1]:
            return False
    return True


def decreasing(arr):
    n = len(arr)

    for i in range(n-1):
        if arr[i] < arr[i+1]:
            return False
    return True


def shortestUnsortedSubarray(arr):
    if increasing(arr) or decreasing(arr):
        return 0
    else:
        return 3


print shortestUnsortedSubarray([9, 10, 11, 7, 12])