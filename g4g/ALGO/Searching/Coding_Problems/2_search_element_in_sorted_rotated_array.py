''' Search an element in a sorted and rotated array '''

'''
   Idea is to find the pivot point, divide the array in 2 sub-arrays and call
   binary search
'''

def find_pivot(arr, low, high):
    # base cases
    if low >= high:
        return -1
    
    mid = int((low + high) / 2)

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    
    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid - 1)
    return find_pivot(arr, mid + 1, high)


def binary_search(arr, low, high, key):
    if high < low:
        return -1

    mid = int((low + high) / 2)

    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binary_search(arr, mid + 1, high, key)
    return binary_search(arr, low, mid - 1, key)


def pivoted_binary_search(arr, key):
    n = len(arr)
    pivot = find_pivot(arr, 0, n-1)

    # If no pivot, then array is sorted
    if pivot == -1:
        return binary_search(arr, 0, n-1, key)
    
    # If pivot is found, compare key with pivot and then search in sub-arrays
    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binary_search(arr, 0, pivot-1, key)
    return binary_search(arr, pivot+1, n-1, key)

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 9
print pivoted_binary_search(arr, key)
