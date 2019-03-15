'''
   Majority element in a sorted array.
'''

# Method 1: Linear search.
# Once found, check if count > n/2, if yes -return else increment count.
# Time - O(n)

# Method 2: Binary Search

def isMajority(arr, x):
    n = len(arr)
    i = binarySearch(arr, 0, n-1, x)
    if i == -1:
        return False
    
    # Check if element in present more than n/2 times.
    if (i + n/2) <= (n-1) and arr[i + n//2] == x: # **
        return True
    return False

def binarySearch(arr, low, high, x):
    if high >= low:
        mid = (low + high) // 2

        '''
           We need to check if x is the first occurrence.
           X is the first occurence if one of the below is True:
           1) arr[mid] == 0 and arr[mid] == x
           2) arr[mid-1] < x and arr[mid] == x
        '''
        if (mid == 0 or x > arr[mid -1]) and (arr[mid] == x): # **
            return mid
        elif x > arr[mid]:
            return binarySearch(arr, mid+1, high, x)
        return binarySearch(arr, low, mid-1, x)
    return -1

print isMajority([1, 2, 3, 3, 3, 3, 10], 3)