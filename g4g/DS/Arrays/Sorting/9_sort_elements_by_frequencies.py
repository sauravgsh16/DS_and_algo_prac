'''
   Sort elements by frequency | Set 1

   Print the elements of an array in the decreasing frequency if 2 numbers
   have same frequency then print the one which came first.

   Input:  arr[] = {2, 5, 2, 8, 5, 6, 8, 8}
   Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6}
'''
# METHOD 1: Using dict to count freq and index.

def sort_by_frequency(arr):
    n = len(arr)
    freq = {}
    index = {}

    for i in range(n):
        if freq.get(arr[i], ''):
            freq[arr[i]] += 1
        else:
            index[arr[i]] = i
            freq[arr[i]] = 1
            
    
    sorted_d = sorted(freq, key=freq.get, reverse=True)
    arr_index = 0
    for i in range(len(sorted_d)):
        if (i + 1) < len(sorted_d):
            if freq[sorted_d[i]] == freq[sorted_d[i+1]]:
                if index[sorted_d[i]] > freq[sorted_d[i+1]]:
                    sorted_d[i], sorted_d[i+1] = sorted_d[i+1], sorted_d[i]
        for _ in range(freq[sorted_d[i]]):
            arr[arr_index] = sorted_d[i]
            arr_index += 1

    return arr

print sort_by_frequency([2, 5, 2, 8, 5, 6, 8, 8])

# METHOD 2 : Can use a BST
# Node: Value, count, index
# Insert node in the tree, if tree already contains the node, increment the count.