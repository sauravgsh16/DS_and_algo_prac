''' Given a sorted and rotated array, find if there is a pair with a given sum '''


def find_pivot(arr, low, high):
    # base cases
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


def find_pair_of_sum(arr, x):
    n = len(arr)
    h = find_pivot(arr, 0, n-1)
    l = h + 1

    while l != h:
        if arr[l] + arr[h] == x:
            return arr[l], arr[h]
        
        if arr[l] + arr[h] > x:
            h = (n + h - 1) % n
        else:
            l = (l + 1) % n
    return -1

arr = [11, 15, 6, 8, 9, 10]
x = 16
print find_pair_of_sum(arr, x)
