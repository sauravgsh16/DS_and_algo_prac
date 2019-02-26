'''
   Move all zeroes to end of array
   Expected time complexity is O(n) and extra space is O(1).
   Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
   Output : arr[] = {1, 2, 4, 3, 5, 0, 0};
'''

def rearrange(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    for i in range(count, n):
        arr[count] = 0
        count += 1
    return arr

def rearrange2(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
    return arr

print rearrange([1, 2, 0, 4, 3, 0, 5, 0])
print rearrange([1, 2, 0, 4, 3, 0, 5, 0])