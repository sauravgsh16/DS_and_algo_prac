''' Interpolation Search '''

'''
   The idea of formula is to return higher value of pos
   when element to be searched is closer to arr[hi]. And
   smaller value when closer to arr[lo]
    
   pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]

   arr[] ==> Array where elements need to be searched
   x     ==> Element to be searched
   lo    ==> Starting index in arr[]
   hi    ==> Ending index in arr[]

   Algo:

   1: In a loop, calculate the value of "pos" using the probe position formula.
   2: If it is a match, return the index of the item, and exit.
   3: If the item is less than arr[pos], calculate the probe position of the
      left sub-array. Otherwise calculate the same in the right sub-array.
   4: Repeat until a match is found or the sub-array reduces to zero.
'''

def interpolation_search(arr, n , x):
    # Find indexes of the two corners
    lo = 0
    hi = n - 1

    # Since array is sorted, an element present in array must be in range
    # defined by the corner values.

    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        if lo == hi:
            if arr[lo] == x:
                return lo
            return -1
        
        # Probing the position with keeping the uniform distribution in mind
        pos = lo + int(
            (float(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo])
        )

        # Condition of target found
        if arr[pos] == x:
            return pos
        
        # If x is larger, x is in the upper part
        if arr[pos] < x:
            lo = pos + 1
        # If x is smaller, x is in the lower part
        else:
            hi = pos - 1
    
    return -1


arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47] 
n = len(arr)
x = 18
print "Element found at index : ", interpolation_search(arr, n, x)
