''' Find closest pair to a given number x, from two sorted arrays '''

def find_pair(arr1, arr2, x):
    diff = 2**32
    l_idx = r_idx = 0
    l = 0
    r = len(arr2) - 1

    while l < len(arr1) and r >= 0:
        if abs(arr1[l] + arr2[r] - x) < diff:
            l_idx = l
            r_idx = r
            diff = abs(arr1[l] + arr2[r] - x)
        
        if arr1[l] + arr2[r] > x:
            r -= 1
        else:
            l += 1

    return arr1[l_idx], arr2[r_idx]

arr1 = [1, 4, 5, 7]
arr2 = [10, 20, 30, 40]
x = 32

arr3 = [1, 4, 5, 7]
arr4 = [10, 20, 30, 40]
y = 50

print find_pair(arr1, arr2, x)
print find_pair(arr3, arr4, y)
