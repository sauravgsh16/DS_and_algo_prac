''' Find the repeating and the missing element in an array '''

'''
   Use elements as Index and mark the visited places)

   Approach:
   Traverse the array. While traversing, use the absolute value of every element
   as an index and make the value at this index as negative to mark it visited.
   If something is already marked negative then this is the repeating element.
   To find missing, traverse the array again and look for a positive value.
'''

def find_repeated_and_missing(arr):
    n = len(arr)
    for i in range(n):
        if arr[abs(arr[i])-1] > 0:
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
        else:
            print "Repeating element is", abs(arr[i])
    
    print arr

    for i in range(n):
        if arr[i] > 0:
            print "Missing element is", i + 1


arr = [7, 3, 4, 5, 5, 6, 2, 7]
find_repeated_and_missing(arr)
