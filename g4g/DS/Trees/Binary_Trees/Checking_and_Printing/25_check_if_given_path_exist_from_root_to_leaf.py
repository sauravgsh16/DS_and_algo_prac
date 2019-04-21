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
    
    if root.val == path[index] and \
        root.left is None and root.right is None and \
        (index == n- 1):
        return True
    
    return root.val == path[index] and \
        (path_exists(root.left, path, n, index + 1) or
         path_exists(root.right, path, n, index + 1))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

path1 = [1, 2, 4]
path2 = [1, 3, 6]
path3 = [1, 3, 7]
for path in [path1, path2, path3]:
    assert(path_exists(root, path, len(path), 0))
print 'All passed'