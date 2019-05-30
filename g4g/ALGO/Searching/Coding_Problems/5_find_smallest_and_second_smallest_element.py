''' Find smallest and second smallest element in an array '''

def find_smallest_and_second_smallest(arr):
    first = second = 2**32

    for i in range(len(arr)):
        if arr[i] < first:
            second = first
            first = arr[i]

        elif arr[i] != first and arr[i] < second:
            second = arr[i]
    print first, second


arr = [12, 13, 1, 10, 34, 5]
find_smallest_and_second_smallest(arr)
