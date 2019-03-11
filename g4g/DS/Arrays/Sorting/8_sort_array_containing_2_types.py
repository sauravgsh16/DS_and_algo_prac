'''
   Sort an array containing two types of elements
   We are given an array of 0s and 1s in random order. 
   Segregate 0s on left side and 1s on right side of the array. 
   Traverse array only once.

   Input :  arr[] = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
   Output : arr[] = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
'''

def segregageZeroAndOne(arr):
    n = len(arr)

    t0 = 0
    t1 = n - 1

    while (t0 < t1):
        if arr[t0 > 0]:
            arr[t0], arr[t1] = arr[t1], arr[t0]
            t1 -= 1
        else:
            t0 += 1
    
    return arr

print segregageZeroAndOne([1, 1, 0, 1, 0, 0, 1])