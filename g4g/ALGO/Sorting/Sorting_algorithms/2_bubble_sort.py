''' Bubble sort '''


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False # For optimization
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # We no elements are swapped, in the inner loop, break
        if swapped == False:
            break

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print arr
