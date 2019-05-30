''' Binary Search - sorted data '''

def binary_search(arr, l, r, n):
    # Base Case
    if r >= l:
        mid = l + (r - l) / 2

        if arr[mid] == n:
            return True
        
        elif n < arr[mid]:
            return binary_search(arr, l, mid - 1, n)
        else:
            return binary_search(arr, mid + 1, r, n)
    else:
        return False


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10
l = len(arr) - 1
print binary_search(arr, 0, l, n)