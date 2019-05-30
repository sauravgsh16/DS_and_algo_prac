''' Find a fixed point in a given array '''

'''
   Fixed point is defined as the index i such that arr[i] is equal to i
'''

# We can use linear search

# In below method we utilize Binary Search

def find_fixed_point(arr, low, high):
    if high < low:
        return -1
    
    mid = (low + high) / 2
    if mid == arr[mid]:
        return mid
    
    if mid > arr[mid]:
        return find_fixed_point(arr, mid+1, high)
    return find_fixed_point(arr, low, mid-1)

arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
print find_fixed_point(arr, 0, len(arr)-1)
