''' Find the Missing Number '''

'''
   Get sum of number:
      total = n * (n + 1) / 2
   Substract all the number from sum and we get the missing number
'''

def get_missing_no(arr):
    n = len(arr)

    total = (n+1) * (n+2) / 2
    arr_sum = sum(arr)
    return total - arr_sum


arr = [1, 2, 4, 6, 3, 7, 8]
missing_no = get_missing_no(arr)
print missing_no
