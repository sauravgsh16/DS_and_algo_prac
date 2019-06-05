''' Given a sorted array and a number x, find pair whose sum is closest to x '''


def find_pair(arr, x):
    diff = 2**32
    i = 0
    j = len(arr) - 1
    l_idx = r_idx = 0

    while i < j:
        if abs(arr[i] + arr[j] - x) < diff:
            l_idx = i
            r_idx = j
            diff = abs(arr[i] + arr[j] - x)
        
        if arr[i] + arr[j] > x:
            j -= 1
        else:
            i += 1
    
    return arr[l_idx],  arr[r_idx]


arr = [10, 22, 28, 29, 30, 40]
x = 54
print find_pair(arr, x)
