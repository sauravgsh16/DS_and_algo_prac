''' Find the maximum element in an array which is first increasing and then decreasing '''

'''
   Eg: arr = [8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1]
   Output: 500

   Linear Search:
   We can search for the maximum element and once we come across an element less
   than max, we break and return max
'''

'''
   Binary Search
   
   We can modify the standard Binary Search algorithm for the given type of arrays.
   1) If the mid element is greater than both of its adjacent elements, 
      then mid is the maximum.
   2) If mid element is greater than its next element and smaller than the
      previous element then maximum lies on left side of mid.
      Example array: {3, 50, 10, 9, 7, 6}
   3) If mid element is smaller than its next element and greater than the
      previous element then maximum lies on right side of mid.
      Example array: {2, 4, 6, 8, 10, 3, 1}
'''

def find_element(arr, low, high):
    # Base Case: Only one element is present in arr[low..high]
    if high == low:
        return arr[low]
    
    # If there are two elements and first is greater, then
    # the first element is maximum
    if high == low + 1 and arr[low] >= arr[high]:
        return arr[low]

    # If there are two elements and second is greater, then 
    # the second element is maximum
    if high == low + 1 and arr[high] > arr[low]:
        return arr[high]
    
    mid = (low + high) / 2

    if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
        return mid
    
    if arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
        return find_element(arr, mid+1, high)
    else:
        return find_element(arr, low, mid-1)


arr = [1, 3, 50, 10, 9, 7, 6]
print find_element(arr, 0, len(arr)-1)
