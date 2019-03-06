'''
   Find the smallest and second smallest elements in an array

   Input:  arr[] = {12, 13, 1, 10, 34, 1}
   Output: The smallest element is 1 and second Smallest element is 10
'''
import sys

def smallestandsecond(arr):
    n = len(arr)

    smallest = sys.maxsize
    second = sys.maxsize

    for i in range(n):
        if arr[i] < smallest:
            second = smallest
            smallest = arr[i]
        
        elif arr[i] < second and arr[i] == smallest:
            second = arr[i]
    
    return smallest, second

print smallestandsecond([12, 13, 10, 34, 1])