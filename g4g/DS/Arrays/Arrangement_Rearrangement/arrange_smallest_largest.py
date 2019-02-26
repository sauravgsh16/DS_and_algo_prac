# -*- coding: utf-8 -*-
'''
   Rearrange an array in order – smallest, largest, 2nd smallest, 2nd largest

   Input : arr[] = [5, 8, 1, 4, 2, 9, 3, 7, 6]
   Output: arr[] = [1, 9, 2, 8, 3, 7, 4, 6, 5]
'''

def rearrange(arr):
    n = len(arr)

    arr.sort()
    temp = [None] * n

    arrIndex = 0

    i, j = 0, n-1

    while i <= n // 2 or j > n // 2:
        temp[arrIndex] = arr[i]
        arrIndex += 1
        if i != j:
            temp[arrIndex] = arr[j]
            arrIndex += 1
        i += 1
        j -= 1
    return temp
        

print rearrange([5, 8, 1, 4, 2, 9, 3, 7, 6])