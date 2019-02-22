''' Rotate an array of size 'n' by 'd' elements'''

def leftRotate(arr, d, n):
    for i in range(d):
        leftRotateOne(arr, n)

def leftRotateOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def printArray(arr):
    for ele in arr:
        print ele

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    leftRotate(arr, 4, 5)
    printArray(arr)
