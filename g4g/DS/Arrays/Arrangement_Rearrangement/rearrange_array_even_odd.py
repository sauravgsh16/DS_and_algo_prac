'''
   Rearrange array such that arr[i] >= arr[j] if i is even and arr[i]<=arr[j] 
   if i is odd and j < i
   Given an array of n elements. Our task is to write a program to rearrange
   the array such that elements at even positions are greater than all elements
   before it and elements at odd positions are less than all elements before it.

   Input : arr[] = {1, 2, 3, 4, 5, 6, 7}
   Output : 4 5 3 6 2 7 1

   Input : arr[] = {1, 2, 1, 4, 5, 6, 8, 8} 
   Output : 4 5 2 6 1 8 1 8
'''
import unittest

def rearrage_array(arr):
    lenght = len(arr)
    even = int(lenght / 2)
    odd = lenght - even

    temp = [None] * lenght

    for i in range(lenght):
        temp[i] = arr[i]
    temp.sort()

    # Fill up the odd indexes
    j = odd - 1
    for i in range(0, lenght, 2):
        arr[i] = temp[j]
        j -= 1
    
    # Fill up the even indexes
    j = odd
    for i in range(1, lenght, 2):
        arr[i] = temp[j]
        j += 1

    return arr


class TestRearrange(unittest.TestCase):
    A = [1, 2, 1, 4, 5, 6, 8, 8]
    R = [4, 5, 2, 6, 1, 8, 1, 8]

    def test_rearrange(self):
        result = rearrage_array(self.A)
        self.assertEqual(result, self.R)

if __name__ == '__main__':
    unittest.main()
