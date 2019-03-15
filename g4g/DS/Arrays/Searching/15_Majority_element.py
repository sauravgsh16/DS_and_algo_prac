'''
   Majority Element
   A majority element in an array A[] of size n is an element that appears 
   more than n/2 times (and hence there is at most one such element)

   Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
   Output : 4

   Input : {3, 3, 4, 2, 4, 4, 2, 4}
   Output : No Majority Element
'''

# Method 1: Nested Loops

# Method 2: Binary Search Tree
# Insert elements in the BST one by one. If element is present,
# increment the count. At any stage, if count > n/2 then return
# Time complexity is O(n^2) if a binary tree is used.
# Time complexity become O(nlogn) in case of self balancing BST
# Space - O(n)

# Method 3: Moore's Voting Algorithm.
# Only works when a majority is present.
# Time - O(n), space - O(1)
# Step 1: Finding a candidate.
# Basic idea is if we cancel out each occurrence of an element e,
# with all other elements that are different from e, e will exist
# till end if it in majority.

'''
    Example :
    Let the array be A[] = 2, 2, 3, 5, 2, 2, 6

    Initialize maj_index = 0, count = 1
    Next element is 2, which is same as a[maj_index] => count = 2
    Next element is 3, which is different from a[maj_index] => count = 1
    Next element is 5, which is different from a[maj_index] => count = 0
    Since count = 0, change candidate for majority element to 5 => maj_index = 3, count = 1
    Next element is 2, which is different from a[maj_index] => count = 0
    Since count = 0, change candidate for majority element to 2 => maj_index = 4
    Next element is 2, which is same as a[maj_index] => count = 2
    Next element is 6, which is different from a[maj_index] => count = 1
    Finally candidate for majority element is 2.
'''

def findCandidate(arr):
    maj_index = 0
    count = 1
    n = len(arr)
    for i in range(n):
        if arr[i] == arr[maj_index]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1
    return arr[maj_index]


# Step 2: Check if the element obtained in step 1 is majority element or not :

def isMajority(arr, candidate):
    count = 0
    for i in range(len(arr)):
        if arr[i] == arr[candidate]:
            count += 1
    
    if count > len(arr)/2:
        return True
    return False

arr= [1, 3, 3, 3, 3, 1, 2]
print isMajority(arr, findCandidate(arr))


# METHOD 4: Using Hash table to store count.
# Time - O(n), space - O(n)