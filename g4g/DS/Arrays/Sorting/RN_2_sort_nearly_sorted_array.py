'''
   
'''

# Function to sort an array using
# insertion sort
def insertionSort():
    n = len(arr)

    i, key, j = 0, 0, 0
    for i in range(n):
        key = arr[i]
        j = i-1
    # Move elements of arr[0..i-1], that are
    # greater than key, to one position
    # ahead of their current position.
    # This loop will run at most k times
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j = j - 1
        arr[j + 1] = key

arr = [6, 5, 3, 2, 8, 10, 9]
insertionSort()
print arr

# CONTAINS ALTERNATE METHOD USING MIN HEAP. NEED TO UNDERSTAND