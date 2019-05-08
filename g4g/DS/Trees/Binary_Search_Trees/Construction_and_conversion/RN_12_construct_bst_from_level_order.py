''' Construct BST from level order traversal '''
import sys

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class NodeDetails(object):
    def __init__(self, ptr):
        self.ptr = ptr
        self.min = None
        self.max = None


def construct_BST(arr, n):
    if n == 0:
        return
    # Queue to store node details
    queue = []
    # Index variable to access array elements
    i = 0

    root = Node(arr[i])
    i += 1
    nodeDetail = NodeDetails(root)
    nodeDetail.min = INT_MIN
    nodeDetail.max = INT_MAX

    queue.append(nodeDetail)

    while i < n:
        temp = queue.pop(0)

        # check whether there are more elements  
        # in the arr and arr[i] can be left child  
        # of 'temp.ptr' or not
        if i < n and (arr[i] < temp.ptr.val and arr[i] > temp.min):
            # Create NodeDetails for newNode and add it to the queue
            newNode = Node(arr[i])
            newNodeDetail = NodeDetails(newNode)
            newNodeDetail.min = temp.min
            newNodeDetail.max = temp.ptr.val
            queue.append(newNodeDetail)
            # make this 'newNode' as left child of 'temp.ptr'
            temp.ptr.left = newNode
            # Increment i
            i += 1

        # check whether there are more elements  
        # in the arr[] and arr[i] can be right child  
        # of 'temp.ptr' or not
        if i < n and (arr[i] > temp.ptr.val and arr[i] < temp.max):
            newNode = Node(arr[i])
            newNodeDetail = NodeDetails(newNode)
            newNodeDetail.min = temp.ptr.val
            newNodeDetail.max = temp.max
            queue.append(newNodeDetail)
            # make this newNode as right child of temp.ptr
            temp.ptr.right = newNode
            # Increment i
            i += 1
    return root


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.val,
    inorder(root.right)


arr = [7, 4, 12, 3, 6, 8, 1, 5, 10]
root = construct_BST(arr, len(arr))
inorder(root)
