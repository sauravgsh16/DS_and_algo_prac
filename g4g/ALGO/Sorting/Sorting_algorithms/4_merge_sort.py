''' Merge Sort '''

def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) / 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    # If any element was not processed in left arr
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    # If any element was not processed in the right arr
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


arr = [32,18,29,63,37,54,89,39,11,38,41,77,35,40,66,37,20,81,91]
merge_sort(arr)

print arr