'''
   Prefix sum array
   prefixSum[i] is arr[0] + arr[1] + arr[2] ... arr[i].

   Input  : arr[] = {10, 20, 10, 5, 15}
   Output : prefixSum[] = {10, 30, 40, 45, 60}
'''

def prefixSum(arr):
    n = len(arr)
    prefixArr = []
    prefixArr.append(arr[0])
    for i in range(1, n):
        prefixArr.append(prefixArr[i-1] + arr[i])
    return prefixArr

print prefixSum([10, 20, 10, 5, 15])
