'''
   Find the only repetitive element between 1 to n-1
   Input  : a[] = {1, 3, 2, 3, 4}
   Output : 3
'''

# MULTIPLE METHODS

# Method 1
# Using nested loops. O(n^2)

# Method 2
# Using the sum method. 
# Find sum of natural number, n(n-1)/2
# Find the sum of the number present in the array.
# Subtract to find the missing element.
# Time - O(n) - space - O(1)
def findele1(arr):
    n = len(arr)
    s = sum(arr)
    natural_sum = (n * (n - 1))/ 2

    return s - natural_sum

print findele1([9, 8, 2, 6, 1, 8, 5, 3, 4, 7])


# Method 3:
# Use hash table
# Time - O(n) - space - O(n)

# Method 4:
# Use XOR property:
#   1) x ^ y = y ^ x, 
#   2) x ^ x = 0
# Time - O(n) - space - O(1)
# 1) Compute XOR of elements from 1 to n-1.
# 2) Compute XOR of array elements.
# 3) XOR of above two would be our result.
def findele2(arr):
    res = 0
    n = len(arr)
    for i in range(0, n-1):
        res = res ^ (i+1) ^ arr[i]
    res = res ^ arr[n-1]
    return res

print findele2([9, 8, 2, 6, 1, 8, 5, 3, 4, 7])


# METHOD 5:
# Indexing
# Time - O(n) - space - O(1)

def findele3(arr):
    n = len(arr)
    repeated_element = -1
    for i in range(n):
        element = arr[abs(arr[i])]
        if element < 0:
            repeated_element = abs(arr[i])
            break
        # Change element in index to negative
        arr[abs(arr[i])] = -arr[abs(arr[i])]
    
    return repeated_element
# Driver code 
arr = [9, 8, 2, 6, 1, 8, 5, 3, 4, 7] 
print findele3(arr)
