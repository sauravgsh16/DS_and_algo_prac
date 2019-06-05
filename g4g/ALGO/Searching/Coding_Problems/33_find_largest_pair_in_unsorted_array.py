''' Find sum of largest pair in unsorted array '''

# Problem boils down to finding the largest and second largest number in array


def find_largest_pair(arr):
    if arr[0] < arr[1]:
        first = arr[1]
        second = arr[0]
    else:
        first = arr[0]
        second = arr[1]
    
    for i in range(2, len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            second = arr[i]
    
    return first + second


arr = [12, 34, 10, 6, 40]
print find_largest_pair(arr)
