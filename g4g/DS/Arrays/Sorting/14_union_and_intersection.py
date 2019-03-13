'''
   Union and Intersection of two sorted arrays

   Input : arr1[] = {1, 3, 4, 5, 7}
           arr2[] = {2, 5, 6} 
   Output : Union : {1, 2, 3, 4, 5, 6, 7} 
            Intersection : {3, 5}
'''

def union(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    i = k = 0
    result = []

    while i < m and k < n:
        while i < m and arr1[i] <= arr2[k]:
            result.append(arr1[i])
            i += 1
        while k < n and arr2[k] < arr1[i]:
            if arr2[k] in result:
                k += 1
                continue
            else:
                result.append(arr2[k])
            k += 1
    while i < m:
        result.append(arr1[i])
        i += 1
    while k < n:
        result.append(arr2[k])
        k += 1
    return result


def intersection(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    i = k = 0
    result = []
    while i < m and k < n:
        if arr1[i] < arr2[k]:
            i += 1
        elif arr2[k] < arr1[i]:
            k += 1
        else:
            result.append(arr1[i])
            i += 1
            k += 1
    return result

m = [1, 3, 4, 5, 7]
n = [2, 3, 5, 6]
print union(m, n)
print intersection(m, n)
