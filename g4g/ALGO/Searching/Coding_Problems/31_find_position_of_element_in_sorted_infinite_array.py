''' Find the position of an element in a sorted array of infinite number '''

'''
   We need to find the lower and upper limit first.
   Once we have the boundary, we can apply binary search to find element
'''

def binary_search(arr, low, high, x):
    if low > high:
        return -1
    
    mid = low + ((high - low) / 2)

    if arr[mid] == x:
        return mid
    
    if arr[mid] > x:
        return binary_search(arr, low, mid-1, x)
    return binary_search(arr, mid+1, high, x)


def find_position(arr, x):
    low = 0
    high = 1
    val = arr[0]

    while val < x:
        low = high
        high = 2 * high
        val = arr[high]
    
    return binary_search(arr, low, high, x)


arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
x = 10
print find_position(arr, x)
