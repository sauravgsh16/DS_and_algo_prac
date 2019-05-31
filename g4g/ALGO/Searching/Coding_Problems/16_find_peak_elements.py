'''
   Find peak elements

   Peak elements are elements which are greater than it's neighbours.
   For corner elements, we compare it with only element
'''

def find_peak_element(arr, low, high, n):
    mid = (low + high) / 2

    if (mid == 0 or arr[mid-1] < arr[mid]) and \
        (mid == n-1 or arr[mid] > arr[mid+1]):
        return  mid
    
    elif mid < n-1 and arr[mid] < arr[mid+1]:
        return find_peak_element(arr, mid + 1, high, n)
    else:
        return find_peak_element(arr, low, mid-1, n)


def find_peak(arr):
    n = len(arr)
    idx = find_peak_element(arr, 0, n-1, n)
    return arr[idx]

arr = [ 12, 22, 18, 20, 21, 1, 0]
print find_peak(arr)
