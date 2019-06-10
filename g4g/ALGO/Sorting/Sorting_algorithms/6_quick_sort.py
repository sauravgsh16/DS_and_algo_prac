''' Quick Sort '''

'''
   Divide and Conquer Algorithm.
   It picks an element as pivot and partitions the given array arounf the
   picked pivot.

   The key process is quick sort is partition. The process is as:
   Given an array and an element x of an array as pivot, put x at its correct
   partition in sorted array and put all elements smaller than x, before x
   and put all elements greater than x, after x.
'''

# Quick Sort implementation by selecting last element as pivot.

def partition(arr, low, high):
    i = low - 1 # Index of smaller element
    pivot = arr[high] # Selecting last element as pivot

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:

        pivot = partition(arr, low, high)
    
        # Call quick_sort for left and right sides
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n-1)
print arr
