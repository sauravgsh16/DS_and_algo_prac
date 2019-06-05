''' 
   Search an element in a sorted and rotated array 
   BINARY SEARCH FOR ROTATED ARRAY
'''

'''
   This can be done in one pass, without finding the pivot
   Algo:
       1) Find mid = (l + h) / 2
       2) If key is mid point, return mid
       3) ELSE IF arr[l .... mid] is sorted:
            a) If key is lies between l and mid, recur for arr[l ... mid]
            b) Else recur for arr[mid+1 ... h]
       4) ELSE (arr[mid + 1 ... h] must be sorted):
            a) If key lies beyween mid to h, recur for arr[mid +1 .... h]
            b) Else recur for arr[l .... mid] 
'''

def rotated_binary_search(arr, low, high, key):
    if low > high:
        return -1
    
    mid = int((low + high) / 2)
    if arr[mid] == key:
        return mid
    
    if arr[low] <= arr[mid]:
        # That is array is sorted till mid

        if arr[low] <= key and key <= arr[mid]:
            return rotated_binary_search(arr, low, mid-1, key)
        return rotated_binary_search(arr, mid+1, high, key)
    
    # This mean array from mid to high must be sorted
    else:
        if arr[mid] <= key and key <= arr[high]:
            return rotated_binary_search(arr, mid+1, high, key)
        return rotated_binary_search(arr, low, mid-1, key)

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 9
n = len(arr)
print rotated_binary_search(arr, 0, n-1, key)