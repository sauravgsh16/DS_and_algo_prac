'''
   Minimum distance between two numbers
    Input: arr[] = {1, 2}, x = 1, y = 2
    Output: Minimum distance between 1 and 2 is 1.

    Input: arr[] = {3, 4, 5}, x = 3, y = 5
    Output: Minimum distance between 3 and 5 is 2.

    Input: arr[] = {3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3}, x = 3, y = 6
    Output: Minimum distance between 3 and 6 is 4.

    Input: arr[] = {2, 5, 3, 5, 4, 4, 2, 3}, x = 3, y = 2
    Output: Minimum distance between 3 and 2 is 1.
'''
import sys

def minDist(arr, x, y):
    n = len(arr)
    min_dist = sys.maxsize 
  
    #Find the first occurence of any of the two numbers (x or y) 
    # and store the index of this occurence in prev 
    for i in range(n): 
          
        if arr[i] == x or arr[i] == y: 
            prev = i 
            break

    # NOTE : WE NEED TO TRAVERSE THE COMPLETE DATA SET
    while i < n:
        if arr[i] == x or arr[i] == y:
            if arr[i] != arr[prev] and i - prev < min_dist:
                min_dist = i - prev
            prev = i
        i += 1
    
    return min_dist

print minDist([2, 5, 3, 5, 4, 4, 2, 3], 3, 2)