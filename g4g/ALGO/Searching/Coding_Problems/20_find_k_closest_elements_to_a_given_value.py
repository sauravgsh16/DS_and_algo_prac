''' Find k closest elements to a given value in a sorted array '''

def binary_search(arr, low, high, x):
    # base cases
    if arr[high] <= x:
        return high
    
    if arr[low] > x:
        return low
    
    mid = (high + low) / 2

    if arr[mid] <= x and arr[mid+1] > x:
        return mid
    
    if arr[mid] < x:
        return binary_search(arr, mid+1, high, x)
    return binary_search(arr, low, mid-1, x)


def find_k_closest(arr, x, k):
    mid = binary_search(arr, 0, len(arr)-1, x)

    l = mid
    r = mid + 1
    count = 0

    if arr[l] == x:
        l -= 1

    while l >= 0 and r < len(arr) and count < k:
        if x - arr[l] < arr[r] - x:
            print arr[l],
            l -= 1
        else:
            print arr[r],   
            r += 1
        count += 1
    
    # If k is left and r has been exhausted
    while l >= 0 and count < k:
        print arr[l],
        l -= 1
        count += 1
    
    # If k is left and l has been exhausted
    while r < len(arr) and count < k:
        print arr[r],
        r += 1
        count += 1


arr =[12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
k = 10
find_k_closest(arr, 35, k)
