'''
   Mininum distance between two numbers
'''
import sys

def minDist(arr, x, y):
    n = len(arr)
    mindst = sys.maxsize
    prev = 0
    for i in range(n):
        if arr[i] == x or arr[i] == y:
            prev = i
            break
    
    while i < n:
        if arr[i] == x or arr[i] == y:
            if arr[i] != arr[prev] and (i - prev) < mindst:
                mindst = i - prev
            prev = i
        i += 1
    return mindst

print minDist([2, 5, 3, 5, 4, 4, 2, 3], 3, 2)