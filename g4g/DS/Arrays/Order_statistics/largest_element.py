'''
   Largest element of an array
'''

def largestElement(arr):
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

arr = [10, 324, 45, 90, 9808, 40]
print largestElement(arr)