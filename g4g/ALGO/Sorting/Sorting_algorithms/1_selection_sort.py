''' Selection Sort '''

'''
   In this sorting technique, we repeateadly find the minimum element from the
   unsorted part and put it at the beginnning.

   Algorithm maintains 2 subarrays:
   1) Already Sorted
   2) Remaning subarray which is unsorted.
'''

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
    
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print arr