''' Check if a given path from the root to the leaf exists '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


'''
   Solution: O(n) time
   1) We traverse the tree in preorder
   2) When we move down the tree, we move by one index in the path
   3) If current node is equal to path[index], then till this level path is identical
   4) The remaining path will be either in the left or right subtree
   5) If any node is mismatched, we return back and move to right subtree
'''
def path_exists(root, path, n, index):
    if not root:
        # In this case the path array should be exhausted
        return n == 0
    
    if (root.left == None and root.right == None) and \
        root.val == arr[index] and index = len(path) - 1:
        return True
    
    return (index < n and root.val == arr[index]) and \
        (path_exists(root.left, path, n, index + 1) or \
        path_exists(root.right, path, n, index + 1))