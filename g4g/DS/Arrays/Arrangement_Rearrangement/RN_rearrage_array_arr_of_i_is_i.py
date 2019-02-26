'''
   Rearrange an array, such that arr[i] = i
   If value is not prsent, then fill up with -1
'''
A = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]

# ****** NEED TO SEE AGAIN ********

def rearrageIter(arr, n):
    for i in range(n):
        if arr[i] != -1 and arr[i] != i:
            x = arr[i]
            while arr[x] != -1 and arr[x] != x:
                temp = arr[x]
                arr[x] = x
                x = temp
            arr[x] = x

            if arr[i] != -1:
                arr[i] = -1

rearrageIter(A, len(A))
print A