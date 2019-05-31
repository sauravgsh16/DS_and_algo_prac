''' Find a pair with the given difference '''

'''
   Input: arr[] = {5, 20, 3, 2, 50, 80}, n = 78
   Output: Pair Found: (2, 80)
'''

def find_pair(arr, n):
    size = len(arr)
    arr.sort()

    i, j = 0, 1

    while i < size and j < size:
        if i != j and arr[j] - arr[i] == n:
            print arr[i], arr[j]
            return True
        elif arr[j] - arr[i] < n:
            j += 1
        else:
            i += 1
    print "No pair exists"


arr = [5, 20, 3, 2, 50, 80]
n = 78
find_pair(arr, n)
