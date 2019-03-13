'''
   Sort an array of 0s, 1s and 2s
   Input :  {0, 1, 2, 0, 1, 2}
   Output : {0, 0, 1, 1, 2, 2}
'''

def sort(arr):
    n = len(arr)
    low = 0
    high = n - 1
    mid = 0
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

print sort([0, 1, 2, 0, 1, 2])