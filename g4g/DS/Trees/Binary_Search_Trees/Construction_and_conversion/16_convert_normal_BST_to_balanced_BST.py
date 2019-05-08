''' Convert a normal BST to balanced bst '''

# Method:
# Get inorder to get sorted array.
# Recursively use array to insert into tree

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_inorder(root, arr):
    if not root:
        return
    get_inorder(root.left, arr)
    arr.append(root.val)
    get_inorder(root.right, arr)


def create_balanced_tree(arr):
    if len(arr) <= 0:
        return
    mid = len(arr) / 2
    node = Node(arr[mid])
    node.left = create_balanced_tree(arr[:mid])
    node.right = create_balanced_tree(arr[mid+1:])
    return node

def bst_to_balanced_bst(root):
    arr = []
    get_inorder(root, arr)
    root = create_balanced_tree(arr)
    return root

def preorder_traversal(root):
    if not root:
        return
    print root.val,
    preorder_traversal(root.left)
    preorder_traversal(root.right)

root = Node(10)
root.left = Node(8)
root.left.left = Node(7)
root.left.left.left = Node(6)
root.left.left.left.left = Node(5)

preorder_traversal(root)
print '\n'
root = bst_to_balanced_bst(root)
preorder_traversal(root)
