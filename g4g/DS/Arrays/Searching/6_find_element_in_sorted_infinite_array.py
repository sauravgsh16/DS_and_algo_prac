'''
   Find position of an element in a sorted array of infinite numbers
'''

# We need to find the limit of array where we need to search for
# key which is given.

# Thus, we check if the value at the end is equal the first
# element in the array. If not we increase the size by 2 and repeat
# till we find the element.

def binarySearch(arr, left, right, key):
    mid = left + (right - left) // 2
    if arr[mid] == arr[key]:
        return arr[key]
    elif arr[mid] > arr[key]:
        return binarySearch(arr, left, mid-1, key)
    else:
        return binarySearch(arr, mid+1, right, key)

def findPosition(arr, key):

    low, high, val = 0, 1, arr[key]

    while val > arr[high]:
        low = high
        high *= 2
    
    return binarySearch(arr, low, high, key)

# Little mistake in implementation, need to accept value rather than key.
print findPosition([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 5)