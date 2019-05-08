''' Check for Identical BSTs without building the trees '''

# Explanation:
# https://www.ideserve.co.in/learn/check-if-identical-binary-search-trees-without-building-them-set-1

def check_if_BSTs_are_same_util(treeArr1, treeArr2, index1, index2, mini, maxi):

    # find the first element between min and max. 
    # that element would be used as the root of the subtree we are looking to construct
    for i in range(index1, len(treeArr1)):
        if mini < treeArr1[i] and treeArr1[i] < maxi:
            break
    
    #import pdb; pdb.set_trace()
    for k in range(index2, len(treeArr2)):
        if mini < treeArr2[k] and treeArr2[k] < maxi:
            break

    # since we are constructing same part of the trees for both arrays
    # element found should be same. If element not found,
    # then that means we found no node satisfying this condition.
    # If this is the case then this should be the case for both the trees
    if i == len(treeArr1) - 1 and k == len(treeArr2) - 1:
        # no node found for both trees
        return True
    
    if i == len(treeArr1) - 1 or k == len(treeArr2) - 1:
        return False
    
    if treeArr1[i] == treeArr2[k]:
        return check_if_BSTs_are_same_util(treeArr1, treeArr2, i+1, k+1, mini, treeArr1[i]) and \
            check_if_BSTs_are_same_util(treeArr1, treeArr2, i+1, k+1, treeArr1[i], maxi)
    return False


def check_if_BSTs_are_same(treeArr1, treeArr2):
    INT_MAX = 2**32
    INT_MIN = -2**32
    return check_if_BSTs_are_same_util(treeArr1, treeArr2, 0, 0, INT_MIN, INT_MAX)


treeArr1 = [8, 3, 6, 1, 4, 7, 10, 14, 13]
treeArr2 = [8, 10, 14, 3, 6, 4, 1, 7, 13]

print check_if_BSTs_are_same(treeArr1, treeArr2)
