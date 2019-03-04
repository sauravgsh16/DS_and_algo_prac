# -*- coding: utf-8 -*-
'''
   Double the first element and move zero to end
   Given an array of integers of size n. Assume ‘0’ as invalid number
   and all other as valid number. Convert the array in such a way that if next
   valid number is same as current number, double its value and replace the next
   number with 0. After the modification, rearrange the array such that all 0’s
   are shifted to the end.

   Input : arr[] = {2, 2, 0, 4, 0, 8}
   Output : 4 4 8 0 0 0

   Input : arr[] = {0, 2, 2, 2, 0, 6, 6, 0, 0, 8}
   Output :  4 2 12 8 0 0 0 0 0 0
'''

def rearrange(arr):
    n = len(arr)

    for i in range(n-1):
        if arr[i] == arr[i+1]:
            arr[i] = arr[i] * 2
            arr[i+1] = 0
    
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i] , arr[count]
            count += 1
    print arr

rearrange([0, 2, 2, 2, 0, 6, 6, 0, 0, 8])