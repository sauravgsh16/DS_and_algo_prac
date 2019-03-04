'''
   Reorder an array according to given indexes
   Input:  arr[]   = [10, 11, 12];
           index[] = [1, 0, 2];
   Output: arr[]   = [11, 10, 12]
           index[] = [0,  1,  2]
   time : O(n) and space : O(1) 
'''

def reorder(arr, index):
    n = len(index)

    for i in range(n):
        #  While index[i] and arr[i] are not fixed
        while index[i] != i:
            # Store values of the target (or correct)  
            # position before placing arr[i] there 
            oldTargetI = index[index[i]]
            oldTargetE = arr[index[i]]

            # Place arr[i] at its target (or correct) 
            # position. Also copy corrected index for 
            # new position 
            arr[index[i]] = arr[i]
            index[index[i]] = index[i]

            # Copy old target values to arr[i] and 
            # index[i] 
            index[i] = oldTargetI
            arr[i] = oldTargetE

            print oldTargetI, oldTargetE
    return arr

arr = [10, 11, 12]
indexArr = [1, 0, 2]
print reorder(arr, indexArr)
