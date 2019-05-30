''' Max and Min of an array using minimum number of comparisons '''

'''
   We can perform a linear search. Initialize max and min as index1 and index2.
   Then if element is greater than max, update max or is element is smaller than
   min, then update min.

   In the below approach, we select the elements in pairs, which minimizes the
   number of comparisons
'''

def find_min_max(arr):
    n = len(arr)
    if n == 1:
        maxi = arr[0]
        mini = arr[0]
    if n == 2:
        if arr[0] > arr[1]:
            maxi = arr[0]
            mini = arr[1]
        else:
            maxi = arr[1]
            mini = arr[0]
    else:
        if n % 2 == 0:
            if arr[0] > arr[1]:
                maxi = arr[0]
                mini = arr[1]
            else:
                maxi = arr[1]
                mini = arr[0]
            i = 2
        else:
            mini = arr[0]
            maxi = arr[0]
            i = 1
        while i < n -1:
            if arr[i] > arr[i+1]:
                if arr[i] > maxi:
                    maxi = arr[i]
                if arr[i+1] < mini:
                    mini = arr[i+1]
            else:
                if arr[i] < mini:
                    mini = arr[i]
                if arr[i+1] > maxi:
                    maxi = arr[i+1]
            i += 2
    return maxi, mini

arr = [1000, 11, 445, 1, 330, 3000]
print find_min_max(arr)
