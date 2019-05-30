''' Two elements whose sum is closest to zero '''

'''
   Algo:
   1) We sort the array
   2) take 2 indexes: l, r starting for 0 and n-1 resp.
   3) Add values ar l and r
   4) If sum is -ve, increment l, else decrement r
   5) Keep track of min sum.
   6) Repeat while l < r
'''

def elements_closest_to_zero(arr):
    # Sort Array
    arr.sort()

    min_sum = 2**32

    l = 0
    r = len(arr) - 1

    min_l = l
    min_r = r

    while l < r:
        val_sum = arr[l] + arr[r]
        
        if abs(val_sum) < abs(min_sum):  # NOTE: IMPORTANT TO CHECK ABS VALUE
            min_sum = val_sum
            min_l = l
            min_r = r
        if val_sum > 0:
            r -= 1
        else:
            l += 1
    
    print arr[min_l], arr[min_r]


arr = [1, 60, -10, 70, -80, 85]
elements_closest_to_zero(arr)
