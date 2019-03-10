'''
   Sort an array in wave form
   Given an unsorted array of integers, sort the array into a wave like array.
   An array arr[0..n-1] is sorted in wave form if:
   arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= ...
'''

# Method 1:
# Sorting the array and swapping adjacent elements

def wavePattern1(arr):
    n = len(arr)
    arr.sort()

    for i in range(0, n-2, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    
    return arr

print wavePattern1([10, 90, 49, 2, 1, 5, 23])

# Method 2:
# We just care about the element in the even positions
# Steps:

def wavePattern2(arr):
    n = len(arr)

    for i in range(0, n, 2):
        if (i > 0 and arr[i] < arr[i-1]):
            arr[i], arr[i-1] = arr[i-1], arr[i]

        if (i < n-1 and arr[i] < arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    return arr

print wavePattern2([10, 90, 49, 2, 1, 5, 23])