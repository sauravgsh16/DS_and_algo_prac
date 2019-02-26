'''
   Check the number of times a sorted array has been rotated.
'''
import unittest

# Naive implementation
# Linear search of the smallest element in the array. The index will correspond
# to the number of times the array has been rotated.
# O(n) complexity
def countRotation(arr):
    n = len(arr)

    min = arr[0]
    min_index = 0
    for i in range(n):
        if min > arr[i]:
            min = arr[i]
            min_index = i
    return min_index

# Binary Search
# It boils down to finding the pivot

def countRotationBinary(low, high, arr):
    # If array is not rotated at all
    if high < low:
        return 0
    # If array contains only one element
    if high == low:
        return low

    mid = int((low + high) / 2)

    if mid < high and arr[mid] > arr[mid+1]:
        return mid+1
    if mid > low and arr[mid] < arr[mid-1]:
        return mid
    if arr[low] > arr[mid]:
        return countRotationBinary(low, mid-1, arr)
    return countRotationBinary(mid+1, high, arr)


class TestCountRotations(unittest.TestCase):
    ARR = [3, 4, 5, 6, 7, 1, 2]

    def test_naive(self):
        index = countRotation(self.ARR)
        self.assertEqual(index, 5)

    def test_binary_search(self):
        rot = countRotationBinary(0, len(self.ARR)-1, self.ARR)
        self.assertEqual(rot, 5)

if __name__ == '__main__':
    unittest.main()
