'''
   Check if array of size n can represent a bst of n levels.

   Input : 500, 200, 90, 250, 100
   Output : No
             500
            /
          200
          /
         90
           \
           250  # Cannot be part of BST
           /
          100
 
   Input : 5123, 3300, 783, 1111, 890
   Output : Yes
'''

# Method 1: Constuct a binary tree and check if it is a BST

# Method 2:
# Take two variables max_int and min_int
# int_max to mark maximum limit of left subtree
# int_min to mark minimum limit of right subtree
# for each element check:
# if arr[i] > arr[i-1] and arr[i] > int_min and arr[i] < int_max:
#    update int_min = arr[i - 1]
# elif arr[i] > int_min and arr[i] < int_max:
#    update int_max = arr[i - 1]
# else break

import sys

def check_represent_bst(arr):
    int_min = -sys.maxsize
    int_max = sys.maxsize
    flag = True
    n = len(arr)
    for i in range(1, n):
        # This element can be inserted to the  
        # right of the previous element, only  
        # if it is greater than the previous 
        # element and in the range.
        if arr[i] > arr[i - 1] and \
            arr[i] > int_min and arr[i] < int_max:
            int_min = arr[i - 1]
        # This element can be inserted to the  
        # left of the previous element, only  
        # if it is lesser than the previous  
        # element and in the range.  
        elif arr[i] < arr[i - 1] and \
            arr[i] > int_min and arr[i] < int_max:
            int_max = arr[i - 1]
        else:
            flag = False
            break
    return flag

arr = [5123, 3300, 783, 1111, 890]
print check_represent_bst(arr)

