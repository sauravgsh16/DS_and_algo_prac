''' Check if binary tree is a BST '''
import sys

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Method 1
INT_MIN = -sys.maxsize
INT_MAX = sys.maxsize

def is_BST(root):
    return is_BST_util(root, INT_MIN, INT_MAX)


def is_BST_util(node, mini, maxi):
    if not node:
        return True

    if node.val < mini or node.val > maxi:
        return False
    
    return is_BST_util(node.left, mini, node.val-1) and \
        is_BST_util(node.right, node.val+1, maxi)


# Method 2
# Inorder traversal and then check if arr is in ascending order

# We can save on the auxilary space of storing the array, by just
# storing the previous value and checking if current value is greater
# then previous value while traversing in inorder.
prev = None

def is_BST_inorder(root):
    global prev
    if not root:
        return True
    
    if is_BST_inorder(root.left) is False:
        return False
    
    if prev is not None and prev.val > root.val:
        return False
    
    prev = root
    return is_BST_inorder(root.right)

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

print is_BST(root)
print is_BST_inorder(root)