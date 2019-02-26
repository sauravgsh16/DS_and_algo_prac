'''
   Given an array that is sorted and then rotated around an unknown point. 
   Find if the array has a pair with a given sum 'x'. 
   It may be assumed that all elements in the array are distinct.

   Input: arr[] = {11, 15, 6, 8, 9, 10}, x = 16
   Output: true

   Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 35
   Output: true
   There is a pair (26, 9) with sum 35

   Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 45
   Output: false
   There is no pair with sum 45.
'''

'''
Strategy:
   We find the pivot.
   Largest is pivot, smallest is right of pivot.
'''
import unittest

def pairsInSortedRotated(arr, n, sum):
    pivot = findPivot(arr, 0, n-1)
    if pivot == -1:
        left = 0,
        right = n-1
    else:
        left = (pivot + 1) % n
        right = pivot
    
    count = 0

    while (left != right):
        if arr[left] + arr[right] == sum:
            count += 1
            left = (left + 1) % n
            right = (right -1 + n) % n
        elif arr[left] + arr[right] < sum:
            left = (left + 1) % n
        else:
            right = (n + right - 1) % n
    return count

def findPivot(arr, low, high):
    if high < low:
        return -1
    if high == low:
        return low

    mid = int((low + high) / 2)
    if mid < high and arr[mid] > arr[mid+1]:
        return mid
    if mid > low and arr[mid] < arr[mid-1]:
        return mid-1
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid-1)
    return findPivot(arr, mid+1, high)


class TestPairRotatedArray(unittest.TestCase):
    
    def test1_count(self):
        arr = [11, 15, 6, 8, 9, 10]
        count = pairsInSortedRotated(arr, len(arr), 16)
        self.assertEqual(count, 1)

    def test2_count(self):
        arr = [11, 15, 6, 8, 9, 10]
        count = pairsInSortedRotated(arr, len(arr), 45)
        self.assertEqual(count, 0)
    
    def test3_count(self):
        arr = [11, 15, 6, 8, 9, 10]
        count = pairsInSortedRotated(arr, len(arr), 35)
        self.assertEqual(count, 0)


if __name__ == '__main__':
    unittest.main()