'''
   Rearrange positive and negative numbers in O(n) time and O(1) extra space
    
   Input : [-1, 2, -3, 4, 5, 6, -7, 8, 9]
   Output: [9, -7, 8, -3, 5, -1, 2, 4, 6]
'''

def rearrange(arr):
    n = len(arr)
    # Sort array, considering 0 as pivot, with all negative numbers in the
    # beginning of the array.
    # Similar to partition process of quick sort
    # This results in all negative numbers on the left size of 0
    i = -1
    for j in range(n):
        if arr[j] < 0:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    
    pos = i + 1
    neg = 0

    while neg < pos and pos < n and arr[neg] < 0:
        arr[neg], arr[pos] = arr[pos], arr[neg]
        pos += 1
        neg += 2
    return arr

print rearrange([-1, 2, -3, 4, 5, 6, -7, 8, 9])

    
