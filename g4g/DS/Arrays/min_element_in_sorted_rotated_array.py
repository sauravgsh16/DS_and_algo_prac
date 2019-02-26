'''
   Find minimum element in a sorted and rotated array
'''
import unittest

def findMin(low, high, arr):
    if high < low:
        return 0
    if high == low:
        return low
    
    mid = int((low + high) / 2)

    if mid < high and arr[mid] > arr[mid+1]:
        return mid+1
    if mid > low and arr[mid] < arr[mid-1]:
        return mid
    if arr[mid] < arr[low]:
        return findMin(low, mid-1, arr)
    return findMin(mid+1, high, arr)


class TestCountRotations(unittest.TestCase):
    ARR = [3, 4, 5, 6, 7, 1, 2]

    def test_naive(self):
        index = findMin(0, len(self.ARR)-1, self.ARR)
        self.assertEqual(1, self.ARR[index])


if __name__ == '__main__':
    unittest.main()
