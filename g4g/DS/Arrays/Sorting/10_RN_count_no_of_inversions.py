'''
   Count Inversions in an array. Set 1 (Using Merge Sort)
   Inversion Count for an array indicates - how far (or close)
   the array is from being sorted. If array is already sorted then inversion count is 0. 
   If array is sorted in reverse order that inversion count is the maximum. 
   Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

   Example:
   The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
'''

# METHOD 1:
# Nested loop to count all the elements which are smaller than it


# METHOD 2:
# Use merge sort
# NEED TO COMPLETE, HOW TO COUNT INVERSIONS **********
def merge(arr1, arr2):
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[mid:])
    right = merge_sort(arr[:mid])
    return merge(left, right)

def count_inversions(arr):
    #n = len(arr)
    pass

print merge_sort([2, 3, 1, 5, 4])
