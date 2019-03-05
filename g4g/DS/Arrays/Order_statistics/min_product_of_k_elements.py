'''
   Minimum product of k integers in an array of positive Integers
   Input : 198 76 544 123 154 675
         k = 2
   Output : 9348
   We get minimum product after multiplying
   76 and 123.

   Input : 11 8 5 7 5 100
        k = 4
   Output : 1400
'''
# Use a min heap to store the elements.
# Then extract k elements for multiply them

import heapq

def minproduct(arr, k):
    heapq.heapify(arr)
    ans = 1
    count = 0

    while arr and count < k:
        elem = heapq.heappop(arr)
        ans = ans * elem
        count += 1
    
    return ans

arr = [198, 76, 544, 123, 154, 675] 
k = 2
print minproduct(arr, k)
