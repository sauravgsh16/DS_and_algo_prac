'''
   Find a peak element
   Given an array of integers. Find a peak element in it. An array element is 
   peak if it is NOT smaller than its neighbors. For corner elements, 
   we need to consider only one neighbor. 
   For example, for input array {5, 10, 20, 15}, 20 is the only peak element.
   For input array {10, 20, 15, 2, 23, 90, 67}, there are two peak elements: 20 and 90
'''

# Method 1: Linear Search. Find one peak and return it.
# Worst case time complexity - O(n)



# Method 2: Binary Search
# We use Divide and Conquer to find peak in O(logn) time.
# We check if middle element is greater than it's neighbors, then we return it.

def findPeak(arr, low, high, n):
    mid = (low + high) // 2

    if ((mid == 0 or arr[mid-1]) <= arr[mid] and
        (mid == n-1 or arr[mid+1] <= arr[mid])):
        return mid
    # If middle element is not peak and  
    # its left neighbour is greater  
    # than it, then left half must  
    # have a peak element
    elif (mid > 0 and arr[mid-1] > arr[mid]):
        return findPeak(arr, low, mid-1, n)
    # If middle element is not peak and 
    # its right neighbour is greater 
    # than it, then right half must  
    # have a peak element
    return findPeak(arr, mid+1, high, n)

arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print findPeak(arr, 0, n-1, n)