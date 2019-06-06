''' Find the nearest smaller number on the left side in an array '''

'''
   Input:  arr[] = [1, 6, 4, 10, 2, 5]
   Output:          _, 1, 1, 4, 1, 2

   Simple method would be to make use to two loops.
   Outer starting from the 2nd element to n
   Inner starting from i-1 to 0, where i is the current element in outer
'''

def prev_smaller_element(arr):

    n = len(arr)

    # For the first element
    print "_",

    for i in range(1, n):
        #print 'printing i', i
        for j in range(i-1, -2, -1):
            #print j
            if arr[j] < arr[i]:
                print arr[j],
                break
    # If there is no smaller element for the rightmost element in the array,
    # then print "_"
    if j == -1:
        print "_"

arr = [2, 6, 4, 10, 3, 5, 1]
prev_smaller_element(arr)

'''
   For an efficient solution, we can use a stack.
   Stack contains values which have been processed so far and are smaller than
   the value that is being processed
'''

def prev_smaller_element_stack(arr):
    stack = []
    n = len(arr)
    for i in range(n):
        while len(stack) > 0 and stack[-1] > arr[i]:
            stack.pop()
        
        if len(stack) > 0:
            print stack[-1],
        else:
            print "_",
        stack.append(arr[i])

arr = [2, 6, 4, 10, 3, 5, 1]
prev_smaller_element_stack(arr)
