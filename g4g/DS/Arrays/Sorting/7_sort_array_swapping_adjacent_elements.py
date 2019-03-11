'''
   Sort 1 to N by swapping adjacent elements
   Given an array A of size N consisting of elements 1 to N.
   A boolean array B consisting of N-1 elements indicates that if B[i] is 1, 
   then A[i] can be swapped with A[i+1].
   Find out if A can be sorted by swapping elements.
'''

def sortedAfterSwap(arr1, arr2):
    n = len(arr1)
    for i in range(n -1):
        if arr1[i] > arr1[i+1]:
            if arr2[i] != 0:
                arr1[i], arr1[i+1] = arr1[i+1], arr1[i]

    for i in range(0, n) : 
        if (arr1[i] != i + 1) : 
            return False
    return True

A = [1, 2, 5, 3, 4, 6]
B = [0, 1, 1, 1, 0]

C= [2, 3, 1, 4, 5, 6]
D = [0, 1, 1, 1, 1]
print sortedAfterSwap(A, B)
print sortedAfterSwap(C, D)

