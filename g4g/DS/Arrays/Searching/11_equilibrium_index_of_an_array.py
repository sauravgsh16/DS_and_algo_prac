'''
   Equilibrium index of an array
   Equilibrium index of an array is an index such that the sum of
   elements at lower indexes is equal to the sum of elements at higher
   indexes. 
   For example, in an array A:
   Input : A[] = {-7, 1, 5, 2, -4, 3, 0}
   Output : 3
   3 is an equilibrium index, because:
   A[0] + A[1] + A[2]  =  A[4] + A[5] + A[6]
'''

def equiIndex(arr):
    n = len(arr)

    total = sum(arr)
    leftsum = 0

    for i in range(n):
        total -= arr[i]

        if leftsum == total:
            return i
        leftsum += arr[i]

    return -1

arr = [-7, 1, 5, 2, -4, 3, 0] 
print equiIndex(arr)