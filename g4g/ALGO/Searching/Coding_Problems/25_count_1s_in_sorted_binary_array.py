''' Count no of 1s in sorted binary array '''

'''
   Various methods, we can add all the numbers, sum will be equal to the no of 1s.
   O(n)

   Linear Search - O(n)

   We implement a binary search to find the index from where 0 starts
'''

def find_index_binary(arr, low, high):
    if low > high:
        return 0
    
    mid = low + ((high - low) / 2)

    if (mid == high or arr[mid + 1] == 0) and arr[mid] == 1:
        return mid + 1
    
    if arr[mid] == 1:
        return find_index_binary(arr, mid+1, high)
    return find_index_binary(arr, low, mid-1)


def count_1s(arr):
    idx = find_index_binary(arr, 0, len(arr)-1)
    return idx

arr = [1, 1, 0, 0]
print count_1s(arr)
