'''
   k smallest elements in same order using O(1) extra space

   They order of the elements must the same as given in the array
   Input : arr[] = {4, 2, 6, 1, 5}, 
            k = 3
    Output : 4 2 1
    Explanation : 1, 2 and 4 are three smallest 
    numbers and 4 2 1 is their order in given array

    Input : arr[] = {4, 12, 16, 21, 25}, 
                k = 3
    Output : 4 12 16
    Explanation : 4, 12 and 16 are 3 smallest numbers
    and 4 12 16 is their order in given array
'''

def kSmallest(arr, k):
    n = len(arr)

    # For each arr[i], find whether it is a part of n-smallest
    # using concepts of insertion sort

    for i in range(k, n):

        # Find the largest element from first k-elements
        max_var = arr[k-1]
        pos = k - 1
        for j in range(k-2, 0, -1):
            if arr[j] > max_var:
                max_var = arr[j]
                pos = j
        
        # Check if arr[i] is greater than max_var
        # If yes, shift all the smaller elements by 1 position to the left and
        # replace max_var with the smaller element in the right side of k
        if max_var > arr[i]:
            j = pos
            while j < k - 1:
                arr[j] = arr[j+1]
                j += 1
            arr[k-1] = arr[i]
    
    for i in range(k):
        print arr[i],

arr = [4, 12, 10, 9, 20, 25, 5, 3]
kSmallest(arr, 5)