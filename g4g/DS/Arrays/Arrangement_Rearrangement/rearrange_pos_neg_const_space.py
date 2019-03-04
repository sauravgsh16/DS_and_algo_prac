'''
   Rearrange positive and negative numbers with constant extra space
   Given an array of positive and negative numbers, 
   arrange them such that all negative integers
   appear before all the positive integers in the array
   without using any additional data structure like hash table, arrays, etc.
   The order of appearance should be maintained.
   Input:  [12 11 -13 -5 6 -7 5 -3 -6]
   Output: [-13 -5 -7 -3 -6 12 11 6 5]
'''

def rearrange(arr):
    n = len(arr)

    i = -1
    for j in range(n):
        if arr[j] < 0:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    
    return arr

print rearrange([-12, 11, -13, -5, 6, -7, 5, -3, -6])