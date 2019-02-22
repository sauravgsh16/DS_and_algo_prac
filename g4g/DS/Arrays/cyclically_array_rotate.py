''' Cyclic array rotation '''

import unittest

def cyclic_rotate(arr):
    n = len(arr)

    temp = arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    
    arr[0] = temp

class TestRotate(unittest.TestCase):
    
    def test_rotate(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        cyclic_rotate(arr)
        self.assertEqual(arr, [7, 1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()