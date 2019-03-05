'''
   Find all elements in array which have at-least two greater elements
   Input : arr[] = {2, 8, 7, 1, 5};
   Output : 2  1  5

   Input  : arr[] = {7, -2, 3, 4, 9, -1};
   Output : -2  3  4 -1
'''


# METHOD 1
# Naive approach. Nested loop for each element checking against the rest
# O(n^2)
def findElements1(arr):
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] < arr[j]:
                count += 1
        if count >= 2:
            print arr[i],

# METHOD 2:
# Sort array, print element except the last two
# O(nlogn)
def findElements2(arr):
    n = len(arr)
    arr.sort()
    for i in range(0, n-2):
        print arr[i]

# METHOD 3:
# Efficient. O(n)
'''
In second method we simply calculate second maximum element of array and
print all element which is less than or equal to second maximum.
'''
import sys

def findElements3(arr):
    n = len(arr)
    first = -sys.maxsize
    second = -sys.maxsize
    for i in range(n):
        # if current element is greater than first then update both
        # first and second
        if arr[i] > first:
            second = first
            first = arr[i]
        # If current element is in between first and second
        # then update only second
        elif arr[i] > second:
            second = arr[i]
    
    for i in range(n):
        if arr[i] < second:
            print arr[i],

arr = [2, 8, 7, 1, 5]
findElements3(arr)

