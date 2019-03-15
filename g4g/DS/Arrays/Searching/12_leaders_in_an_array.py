'''
   Leaders in an array
   An element is leader if it is greater than all the elements to its right side.
   And the rightmost element is always a leader.
   For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2
'''
import sys

def leaders(arr):
    n = len(arr)

    leader = -sys.maxsize
    for i in range(n-1, -1, -1):
        if arr[i] > leader:
            leader = arr[i]
            print leader,


leaders([16, 17, 4, 3, 5, 2])