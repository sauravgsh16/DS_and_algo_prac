'''
   Minimum number of swaps required to sort an array
   Input : {4, 3, 2, 1}
   Output : 2
   Explanation : Swap index 0 with 3 and 1 with 2 to 
              form the sorted array {1, 2, 3, 4}.

   Input : {1, 5, 4, 3, 2}
   Output : 2
'''
import copy

def minSwaps(arr):
    n = len(arr)
    temp = copy.deepcopy(arr)
    temp.sort()

    first = 0
    last = n - 1
    index = []
    visited = {}
    while first < last:
        if arr[first] == temp[first]:
            first += 1
        else:
            if not visited.get(arr[first], ''):
                visited[arr[first]] = True
                index.append(first)
            else:
                first += 1
        if arr[last] == temp[last]:
            last -= 1
        else:
            if not visited.get(arr[last], ''):
                visited[arr[last]] = True
                index.append(last) 
            else:
                last -= 1
    swaps = len(index) / 2
    return swaps

print minSwaps([1, 5, 4, 3, 2])