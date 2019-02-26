'''
   Reverse a string or array
'''

# ITERATIVE

def reverseIter(arr):
    start = 0
    stop = len(arr) - 1

    while start < stop:
        arr[start], arr[stop] = arr[stop], arr[start]
        start += 1
        stop -= 1
    return arr

print reverseIter([1, 2, 3, 4, 5])

def reverseRecursive(arr, start, stop):
    if start >= stop:
        return
    arr[start], arr[stop] = arr[stop], arr[start]
    reverseRecursive(arr, start+1, stop-1)

arr = [1, 2, 3, 4, 5]
reverseRecursive(arr, 0, 4)
print arr