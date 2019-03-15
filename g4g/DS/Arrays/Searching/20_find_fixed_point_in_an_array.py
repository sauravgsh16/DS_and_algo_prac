'''
   Find a Fixed Point (Value equal to index) in a given array

   Input: arr[] = {-10, -5, 0, 3, 7}
   Output: 3  // arr[3] == 3 

   Input: arr[] = {0, 2, 5, 8, 17}
   Output: 0  // arr[0] == 0 
'''
# Method 1: Linear search

def findFixedPt(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == i:
            return i
    
    return -1

# Method 2: Binary Search

def findFixedPtBinary(arr, low, high):

    if high >= low:

        mid = (low + high) // 2
        if mid == arr[mid]:
            return mid
        if mid > arr[mid]:
            return findFixedPtBinary(arr, mid+1, high)
        return findFixedPtBinary(arr, low, mid-1)
    
    return -1

arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]

print findFixedPt(arr)
n =  len(arr)
print findFixedPtBinary(arr, 0, n-1)
