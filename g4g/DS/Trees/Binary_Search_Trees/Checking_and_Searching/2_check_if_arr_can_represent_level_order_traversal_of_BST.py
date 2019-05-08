''' Check if a given array can represent level order traveral of a BST '''
import sys

INT_MIN = -sys.maxsize
INT_MAX = sys.maxsize

class NodeDetails(object):
    '''
       Stores node's val and min and max
       min and max is used to obtain the range
       of values where the node's left and right
       child should lie.
    '''
    def __init__(self, ptr):
        self.ptr = ptr
        self.min = None
        self.max = None


def check_bst(arr, n):
    if n == 0:
        return
    
    queue = []
    i = 0

    newNode = NodeDetails(arr[i])
    newNode.min = INT_MIN
    newNode.max = INT_MAX
    i += 1

    queue.append(newNode)

    while i != n and len(queue) > 0:
        temp = queue.pop(0)

        if i < n and (arr[i] < temp.ptr and arr[i] > temp.min):
            newNode = NodeDetails(arr[i])
            newNode.min = temp.min
            newNode.max = temp.ptr

            queue.append(newNode)
            i += 1
        
        if i < n and (arr[i] > temp.ptr and arr[i] < temp.max):
            newNode = NodeDetails(arr[i])
            newNode.min = temp.ptr
            newNode.max = temp.max

            queue.append(newNode)
            i += 1

    if i == n:
        return True
    return False


arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]
print check_bst(arr, len(arr))