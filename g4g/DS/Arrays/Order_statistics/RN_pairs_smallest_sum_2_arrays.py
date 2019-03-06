'''
   Find k pairs with smallest sums in two arrays

   Input :  arr1[] = {1, 7, 11}
         arr2[] = {2, 4, 6}
         k = 3
    Output : [1, 2],
            [1, 4],
            [1, 6]
    Explanation: The first 3 pairs are returned 
    from the sequence [1, 2], [1, 4], [1, 6], 
    [7, 2], [7, 4], [11, 2], [7, 6], [11, 4], 
[11, 6]
'''
'''
Method 1 (Simple)

1) Find all pairs and store their sums. Time complexity of this step is O(n1 * n2) 
   where n1 and n2 are sizes of input arrays.
2) Then sort pairs according to sum. Time complexity of this step is 
   O(n1 * n2 * log (n1 * n2))
'''


'''
Method 2 (Efficient)

We one by one find k smallest sum pairs, starting from the least sum pair.

'''