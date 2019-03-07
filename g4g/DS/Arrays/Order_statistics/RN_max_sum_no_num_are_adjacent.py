'''
   Maximum sum such that no two elements are adjacent

   Input : arr[] = {5, 5, 10, 100, 10, 5}
   Output : 110

   Input : arr[] = {1, 2, 3}
   Output : 4

   Input : arr[] = {1, 20, 3}
   Output : 20
'''

def maxSum(arr):
    n = len(arr)

    incl = 0
    excl = 0

    for i in range(n):
        if excl > incl:
            new_excl = excl
        else:
            new_excl = incl
        
        incl = excl + arr[i]
        excl = new_excl
    return excl if excl > incl else incl

print maxSum([5, 5, 10, 100, 10, 5])
print maxSum([1, 2, 3])
print maxSum([1, 20, 3])