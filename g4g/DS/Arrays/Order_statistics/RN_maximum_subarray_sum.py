'''
   Maximum subarray sum in O(n) using prefix sum
                           -----------------
   Input1 : arr = {-2, -3, |4, -1, -2, 1, 5,| -3}
                           ------------------
   Output1 : 7
'''

'''
   KADANE's Algorithm

    Initialize:
        max_so_far = 0
        max_ending_here = 0

    Loop for each element of the array
        (a) max_ending_here = max_ending_here + a[i]
        (b) if(max_ending_here < 0)
                max_ending_here = 0
        (c) if(max_so_far < max_ending_here)
                max_so_far = max_ending_here
    return max_so_far
'''

def maxSubArraySum(arr, n):
    max_so_far = 0
    max_ending_here = 0

    for i in range(n):
        max_ending_here += arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        
        if max_ending_here < 0:
            max_ending_here = 0
    
    return max_so_far

b = [-2, -3, 4, -1, -2, 1, 5, -3]
a = [4, -8, 9, -4, 1, -8, -1, 6]
print maxSubArraySum(a, len(a))