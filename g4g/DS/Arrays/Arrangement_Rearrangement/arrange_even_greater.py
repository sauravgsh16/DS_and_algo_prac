'''
   Rearrange array such that even positioned are greater than odd
   Given an array A of n elements, sort the array according to the following relations :
   A[i] >= A[i-1]  , if i is even.
   A[i] <= A[i-1]  , if i is odd.
'''
'''
 Strategy: Sort arr, then fill up all even position (n/2) with (n/2) maximum nos.
'''

def rearrange(arr):
    n = len(arr)
    arr.sort()

    res = [None] * n
    p = 0
    q = n - 1

    for i in range(n):
        if (i + 1) % 2 == 0:
            res[i] = arr[q]
            q -= 1
        else:
            res[i] = arr[p]
            p += 1
    return res

print rearrange([1, 3, 2, 2, 5])