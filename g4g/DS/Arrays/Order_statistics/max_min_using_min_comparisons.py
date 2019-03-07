'''
   Find max and min of an array with minimum number of comparisons
'''

def minMax(arr):
    n = len(arr)

    if n % 2 == 0:
        if arr[0] < arr[1]:
            minarr = arr[0]
            maxarr = arr[1]
        else:
            minarr = arr[1]
            maxarr = arr[0]
        i = 2
    else:
        minarr, maxarr = arr[0]
        i = 1
    
    while i < n-1:
        if arr[i] > arr[i+1]:
            if arr[i] > maxarr:
                maxarr = arr[i]
            if arr[i+1] < minarr:
                minarr = arr[i+1]
        else:
            if arr[i+1] > maxarr:
                maxarr = arr[i+1]
            if arr[i] < minarr:
                minarr = arr[i]
        i += 2
    return minarr, maxarr

print minMax([1000, 11, 445, 1, 330, 3000])
