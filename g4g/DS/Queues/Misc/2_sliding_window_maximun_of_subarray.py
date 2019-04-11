''' Sliding window maximum of all subarrays of size k '''

import sys

def print_maximum(arr, k):
    max_int = -sys.maxsize
    for i in range(k):
        if arr[i] > max_int:
            max_int = arr[i]
        else:
            max_int = val

    for i in range(k, len(arr)):
        print max_int,
        if arr[i] > max_int:
            max_int = arr[i]
    print max_int

arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
print_maximum(arr, 3)