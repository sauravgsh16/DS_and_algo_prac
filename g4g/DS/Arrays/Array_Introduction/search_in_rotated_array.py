'''
   An element in a sorted array can be found in O(log n) time via binary search.
   But suppose we rotate an ascending order sorted array at some pivot unknown
   to you beforehand. So for instance, 1 2 3 4 5 might become 3 4 5 1 2.   
'''

'''
Strategy

1) Find pivot
2) If not pivot, then array not rotated - Apply normal binary search
3) If pivot, return if pivot == element to search
4) If arr[0] < element - search in left of pivot
   else, search in right of pivot
'''
import unittest


def pivotedBinarySearch(arr, key):
    n = len(arr)
    # Find Pivot
    pivot = findPivot(arr, 0, n-1)

    if pivot == -1:
        # array has not been rotated
        return binarySearch(arr, 0, n-1, key)
    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binarySearch(arr, 0, pivot-1, key)
    return binarySearch(arr, pivot+1, n-1, key)

def findPivot(arr, low, high):
    if high < low:
        return -1
    if high == low:
        return low
    
    mid = int((low + high) / 2)
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid-1)
    return findPivot(arr, mid+1, high)


def binarySearch(arr, low, high, key):
    if low > high:
        return -1

    mid = int((low + high) / 2)

    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarySearch(arr, (mid+1), high, key)
    return binarySearch(arr, low, (mid-1), key)


class TestPivotedBinarySearch(unittest.TestCase):

    def test_search(self):
        arr = [3, 4, 5, 6, 7, 1, 2]
        index = pivotedBinarySearch(arr, 7)
        self.assertEqual(index, 4)


if __name__ == '__main__':
    unittest.main()