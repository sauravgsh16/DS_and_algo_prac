''' Linear Search Algorithm '''

def linear_search(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return True
    return False


arr = [2, 3, 4, 10, 20]
n = 10
print linear_search(arr, n)
