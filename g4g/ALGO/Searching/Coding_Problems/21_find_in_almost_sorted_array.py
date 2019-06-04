''' Find in almost sorted array '''

'''
   Given an array which is sorted, but after sorting some elements are moved to
   either of the adjacent positions, i.e., arr[i] may be present at arr[i+1] or arr[i-1]
'''

'''
   Soln:
   Comparing only with middle element is enough,
   as all elements left of mid - 2 will be less than x
   and all elements right of mid + 2 will be greater than x
'''

def binary_search(arr, low, high, x):
    if low > high:
        return -1
    
    mid = low + ((high - low) / 2)

    if arr[mid] == x:
        return x
    
    if mid > low and arr[mid-1] == x:
        return mid - 1
    if mid < high and arr[mid+1] == x:
        return mid + 1
    
    if arr[mid] > x:
        return binary_search(arr, low, mid-1, x)
    return binary_search(arr, mid+1, high, x)


arr = [3, 2, 10, 4, 40]
x = 4
print binary_search(arr, 0, len(arr)-1, x)
