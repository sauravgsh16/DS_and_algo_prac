'''
   Two elements whose sum is closest to zero
   Question: An Array of integers is given, both +ve and -ve.
   You need to find the two elements such that their sum is closest to zero.

   For the below array, program should print -80 and 85.
'''

# METHOD 1:
# Compare, each with every other element

def minAbsSumPair(arr):
    n = len(arr)

    min_sum = arr[0] + arr[1]
    min_l = 0
    min_r = 1
    for i in range(n):
        for j in range(i+1, n):
            curr_sum = arr[i] + arr[j]
            if abs(curr_sum) < abs(min_sum):
                min_sum = curr_sum
                min_l = i
                min_r = j
    return arr[min_l], arr[min_r]

print minAbsSumPair([1, 60, -10, 70, -80, 85])

# O(n^2) time complexity

# METHOD 2:
# Sort the array
# Use two pointer, 1st for first index and 2nd for the last index
# If sum is greater than min_sum, then decrement the 2nd pointer else
# if sum is less, then increment the 1st pointer

def minSumPair(arr):
    n = len(arr)

    min_sum = arr[0] + arr[n-1]
    left = min_l = 0
    right = min_r = n - 1

    arr.sort()

    while left < right:
        curr_sum = arr[left] + arr[right]
        if abs(curr_sum) < abs(min_sum):
            min_sum = curr_sum
            min_l = left
            min_r = right
        if curr_sum > 0:
            right -= 1
        else:
            left += 1
    
    return arr[min_l], arr[min_r]

print minSumPair([1, 60, -10, 70, -80, 85])

# Time complexity = O(nlogn) - for sorting + O(n) - when iterating
# Thus: O(nlogn) + O(n) = O(nlogn)