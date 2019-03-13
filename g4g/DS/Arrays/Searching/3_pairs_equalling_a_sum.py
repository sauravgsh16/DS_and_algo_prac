'''
   Given an array A[] and a number x, check for pair in A[] with sum as x
'''

def checkPairs(arr, s):
    n = len(arr)
    arr.sort()
    f = 0
    l = n - 1
    while f < l:
        curr_sum = arr[f] + arr[l]
        if curr_sum < s:
            f += 1
        elif curr_sum > s:
            l -= 1
        else:
            return f, l

print checkPairs([1, 4, 45, 6, 10, -8], 16)