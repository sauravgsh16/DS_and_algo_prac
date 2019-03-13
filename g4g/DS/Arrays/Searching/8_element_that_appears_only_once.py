'''
   Find the element that appears once in an array where every other element appears twice

   Input:  ar[] = {7, 3, 5, 4, 5, 3, 4}
   Output: 7
'''

# METHOD 1- nested loops O(n**2)

# METHOD 2 - Hashing - Time - O(n), space - O(n)

# METHOD 3 - XOR
# x ^ x = 0,  x ^ 0 = x

def find_element(arr):
    n = len(arr)

    res = 0
    for i in range(n):
        print '%d ^ %d' %(res, arr[i])
        res = res ^ arr[i]
        print res
    return res


print find_element([7, 3, 5, 4, 5, 3, 4])
