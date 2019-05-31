''' Find minimum element in sorted rotated array '''


def find_pivot(arr, low, high):
    # base cases
    if low >= high:
        return -1
    
    mid = (low + high) / 2

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    
    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid - 1)
    return find_pivot(arr, mid + 1, high)


def find_min(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    pivot = find_pivot(arr, 0, n-1)
    if pivot == -1:
        return arr[0]
    else:
        return arr[pivot+1]


arr1 = [5, 6, 1, 2, 3, 4] 
print "The minimum element is " + str(find_min(arr1))

arr2 = [1, 2, 3, 4] 
print "The minimum element is " + str(find_min(arr2))

arr3 = [1]
print "The minimum element is " + str(find_min(arr3))

arr4 = [1, 2]
print "The minimum element is " + str(find_min(arr4))

arr5 = [2, 1]
print "The minimum element is " + str(find_min(arr5))

arr6 = [5, 6, 7, 1, 2, 3, 4]
print "The minimum element is " + str(find_min(arr6))

arr7 = [1, 2, 3, 4, 5, 6, 7]
print "The minimum element is " + str(find_min(arr7))


arr8 = [2, 3, 4, 5, 6, 7, 8, 1]
print "The minimum element is " + str(find_min(arr8))

arr9 = [3, 4, 5, 1, 2]
print "The minimum element is " + str(find_min(arr9))
