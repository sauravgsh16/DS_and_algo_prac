'''
   Sum of nodes on the longest path from root to leaf

   If two or more paths compete for the longest path, then path having the
   maximum sum of nodes is considered.
'''
import sys

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sum_of_longest_path_util(root, Sum, Len, maxLen, maxSum):
    if not root:
        if maxLen[0] < Len:
            maxLen[0] = Len
            maxSum[0] = Sum
        elif maxLen[0] == Len and maxSum[0] < Sum:
            maxSum[0] = Sum
        return
    sum_of_longest_path_util(root.left, Sum + root.val, Len + 1, maxLen, maxSum)
    sum_of_longest_path_util(root.right, Sum + root.val, Len + 1, maxLen, maxSum)


def sum_of_longest_path(root):
    if not root:
        return 0
    
    maxSum = [-sys.maxsize]
    maxLen = [0]
    sum_of_longest_path_util(root, 0, 0, maxLen, maxSum)
    print maxSum[0]


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(7)
root.left.right = Node(1)
root.right.left = Node(2)
root.right.right = Node(3)
root.left.right.left = Node(8)

sum_of_longest_path(root)