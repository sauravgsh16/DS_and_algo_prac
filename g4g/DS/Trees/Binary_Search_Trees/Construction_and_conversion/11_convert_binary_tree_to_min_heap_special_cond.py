'''
   Convert a binary Searh tree to min-heap such that, all node on left subtree
   is less than all nodes in the right subtree
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_traversal(root, arr):
    if not root:
        return
    inorder_traversal(root.left, arr)
    arr.append(root.val)
    inorder_traversal(root.right, arr)


def get_inorder(root):
    arr = []
    inorder_traversal(root, arr)
    return arr

def convert_preorder(root, arr):
    if not root:
        return
    root.val = arr.pop(0)
    convert_preorder(root.left, arr)
    convert_preorder(root.right, arr)

def bst_to_min_heap(root):
    inorder = get_inorder(root)
    convert_preorder(root, inorder)

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

bst_to_min_heap(root)
print get_inorder(root)