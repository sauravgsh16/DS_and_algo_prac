''' Merge two balanced Binary Search Trees '''

# Method 1:
# Insert one tree to the other.
# While inserting, tree needs to be balanced.
# Thus, inserting elements will have to done in either 
# an AVL tree or a Red Black Tree

# Method 2:
# Inorder of both trees.
# Merge both arrays in sorted order.
# Create a tree from the sorted array

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


def merge_array(arr1, arr2):
    arr = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            arr.append(arr2[j])
            j += 1
        else:
            arr.append(arr1[i])
            i += 1
    while i < len(arr1):
        arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        arr.append(arr2[j])
        j += 1
    return arr

def construct_tree(arr):
    if len(arr) <= 0:
        return
    mid = len(arr) / 2
    node = Node(arr[mid])
    node.left = construct_tree(arr[:mid])
    node.right = construct_tree(arr[mid+1:])
    return node

def merge_two_balanced_trees(r1, r2):
    arr1 = []
    arr2 = []
    inorder_traversal(r1, arr1)
    inorder_traversal(r2, arr2)
    arr = merge_array(arr1, arr2)
    return construct_tree(arr)


def print_inorder(root):
    if not root:
        return
    print_inorder(root.left)
    print root.val,
    print_inorder(root.right)


root1 = Node(100)
root1.left = Node(50)
root1.right = Node(300)
root1.left.left = Node(20)
root1.left.right = Node(70)


root2 = Node(80)
root2.left = Node(40)
root2.right = Node(120)

root = merge_two_balanced_trees(root1, root2)
print_inorder(root)