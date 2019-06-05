'''
   Count the number of pairs whose sum equals given value in sorted rotated array
'''

def find_pivot(arr, low, high):
    if low > high:
        return -1
    
    mid = low + ((high - low) / 2)

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    
    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid-1)
    return find_pivot(arr, mid+1, high)


def count_pairs_with_sum(arr, x):
    n = len(arr)
    high = find_pivot(arr, 0, n-1)
    if high == -1:
        low = 0
        high = n - 1
    else:
        low = high + 1
    
    count = 0
    while low != high:
        if arr[low] + arr[high] == x:
            count += 1
        
        if arr[low] + arr[high] > x:
            high = (n + high - 1) % n
        else:
            low = (low + 1) % n
    
    return count


arr = [11, 15, 6, 7, 9, 10]
x = 16
print count_pairs_with_sum(arr, x)
