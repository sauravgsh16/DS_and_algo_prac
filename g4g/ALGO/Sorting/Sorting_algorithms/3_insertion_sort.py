''' Insertion sort '''

'''
   We take the element and place it at the left part of the array

   eg:
   [12, 11, 13, 5, 6]
   i = 1
   arr = [11, 12, 13, 5, 6]
   i = 2
   arr = [11, 12, 13, 5, 6]
   i = 3
   arr = [5, 11, 12, 13, 6]
   i = 4
   arr = [5, 6, 11, 12, 13]
'''

def insertion_sort(arr):
    n = len(arr)

    for i in range(n):

        # Move elements of arr[0 .. i-1], that are greater than key, to one
        # position ahead of their current position
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print arr
