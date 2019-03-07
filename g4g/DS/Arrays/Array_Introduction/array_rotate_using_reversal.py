''' Rotate an array of size n by d elements '''

'''
   Algorithm:
   Consider arr = [1, 2, 3, 4, 5, 6, 7]
   n = 7, d = 2
   A = [1, 2] (arr[0] - arr[d-1])
   B = [3, 4, 5, 6, 7] (arr[d] - arr[n-1])
   Rotate A and B: 
        Thus,
        Ar = [2, 1] and Br = [7, 6, 5, 4, 3]
   ArB = [2, 1, 3, 4, 5, 6, 7]
   (ArBr)r = [7, 6, 5, 4, 3, 1, 2]
'''
import unittest

def reverseArray(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


def leftRotate(arr, n, d):
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)


class TestRotate(unittest.TestCase):

    def test_rotate(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        leftRotate(arr, 7, 2)
        self.assertEqual(arr, [3, 4, 5, 6, 7, 1, 2])

if __name__ == '__main__':
    unittest.main()
