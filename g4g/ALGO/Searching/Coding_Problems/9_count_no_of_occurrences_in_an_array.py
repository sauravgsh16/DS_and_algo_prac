''' Count number of occurrences (or frequencies) in a sorted array '''

'''
   METHOD 1
   Liner search
'''

'''
   METHOD 2
   Binary Search
   We find the index of the number , then count the occurrence in the left
   and right of index
'''

def binary_search(arr, left, right, x):
    if right < left:
        return -1

    mid = (right + left) / 2

    if arr[mid] == x:
        return mid
    
    if x < arr[mid]:
        return binary_search(arr, left, mid-1, x)
    return binary_search(arr, mid+1, right, x)

def count_occurrence(arr, x):
    idx = binary_search(arr, 0, len(arr)-1, x)

    if idx == -1:
        return 0
    
    # Count elements on the left side
    count = 1
    left = idx - 1
    while left >= 0 and arr[left] == x:
        count += 1
        left -= 1
    
    # Count elements to the right side
    right = idx + 1
    while right <= len(arr) - 1 and arr[right] == x:
        count += 1
        right += 1
    
    return count

'''
   METHOD 3
   Binary Search

   Use binary search to find first occurrence of the number in the array
   and then find last occurrence.

   count = last - first + 1
'''

def count_occurrence_efficient(arr, x):
    n = len(arr)
    f = first(arr, 0, n-1, x)

    if f == -1:
        return 0
    
    l = last(arr, 0, n-1, x, n)

    return l - f + 1

def first(arr, low, high, x):
    if high >= low:
        mid = (low + high) / 2
    
    if (mid == 0 or x > arr[mid-1]) and arr[mid] == x:
        return mid
    elif x > arr[mid]:
        return first(arr, mid+1, high, x)
    else:
        return first(arr, low, mid-1, x)
    return -1

def last(arr, low, high, x, n):
    if high >= low:
        mid = (low + high) / 2
    
    if (mid == n-1 or x < arr[mid+1]) and arr[mid] == x:
        return mid
    elif x > arr[mid]:
        return last(arr, mid+1, high, x, n)
    else:
        return last(arr, low, mid-1, x, n)
    return -1


arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
print count_occurrence(arr, 8)
print count_occurrence_efficient(arr, 2)
