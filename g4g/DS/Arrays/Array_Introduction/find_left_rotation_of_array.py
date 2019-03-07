'''
Quickly find left rotation of an array
'''

'''
Strategy:
We form an array twice the length of the given array and update it with array
content 2 times.
Find the mod of k rotation to lenght of array.
Start from the mod to the lenght of array and print data
'''
import unittest

def quickRotation(arr, k):
    temp = [None] * 2 * len(arr)
    n = len(arr)
    # Preprocess
    for i in range(n):
        temp[i] = temp[i+n] = arr[i]
    
    start = k % n
    result = ''
    for i in range(start, start+n):
        result += str(temp[i])
    return result

class TestQuickRotation(unittest.TestCase):
    ARRAY = [1, 3, 5, 7, 9]

    def test_quickRotation(self):
        self.assertEqual('91357', quickRotation(self.ARRAY, 14))

if __name__ == '__main__':
    unittest.main()
