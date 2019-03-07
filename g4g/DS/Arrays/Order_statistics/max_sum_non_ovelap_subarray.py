'''
   K maximum sums of non-overlapping contiguous sub-arrays
   Input : arr1[] = {4, 1, 1, -1, -3, -5, 6, 2, -6, -2}, 
             k = 3.
   Output : Maximum non-overlapping sub-array sum1: 8, 
         starting index: 6, ending index: 7.
         
         Maximum non-overlapping sub-array sum2: 6, 
         starting index: 0, ending index: 2.
         
         Maximum non-overlapping sub-array sum3: -1, 
         starting index: 3, ending index: 3.
'''
import sys

def kMax(arr, k):
    n = len(arr)
    for num in range(k):

        # Kadane's algorithm
        max_so_far = -sys.maxsize
        max_ending_here = 0

        start = 0
        end = 0
        s = 0
        for i in range(n):
            max_ending_here += arr[i]

            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
                start = s
                end = i
            if max_ending_here < 0:
                max_ending_here = 0
                s = i + 1
        
        print 'Max: ', max_so_far, 'start: ', start, 'end', end

        # Replace all elements of the maximum subarray 
        # by -sys.maxsize. Hence these places cannot form  
        # maximum sum subarray again.
        for i in range(start, end+1):
            arr[i] = -sys.maxsize

arr = [4, 1, 1, -1, -3, -5, 6, 2, -6, -2] 
k = 3
kMax(arr, k)