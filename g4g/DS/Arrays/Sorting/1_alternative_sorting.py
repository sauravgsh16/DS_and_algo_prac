'''
   Alternative Sorting
   Given an array of integers, print the array in such a way that the first element
   is first maximum and second element is first minimum and so on.

   Input : arr[] = {7, 1, 2, 3, 4, 5, 6}
   Output : 7 1 6 2 5 3 4
'''

def altSorting(arr):
    n = len(arr)

    temp = [0] * n

    arr.sort()
    i = 0
    j = n-1
    k = 0
    while (i < j):
        temp[k] = arr[j]
        k += 1
        temp[k] = arr[i]
        k += 1
        j -= 1
        i += 1
        
    if n % 2 != 0:
        temp[k] = (arr[i])
    return temp

print altSorting([7, 1, 2, 3, 4, 5, 6])
