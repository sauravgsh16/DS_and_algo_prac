''' Convert a Binary Tree to a Binary Search Tree '''

'''
   Solution:
   1) Create arr with inorder traversal of tree
   2) Sort the elements in the array
   3) Again traverse the array in inorder form, while traversing replace key
      from the arr.
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def store_inorder(root, arr):
    if not root:
        return
    store_inorder(root.left, arr)
    arr.append(root.val)
    store_inorder(root.right, arr)


def traverse_inorder(root):
    if not root:
        return
    traverse_inorder(root.left)
    print root.val,
    traverse_inorder(root.right)


def replace_val_from_arr_to_tree(arr, root):
    if not root:
        return

    replace_val_from_arr_to_tree(arr, root.left)
    root.val = arr.pop(0)  # Pop first value from arr
    replace_val_from_arr_to_tree(arr, root.right)


def binary_tree_to_bst(root):
    if not root:
        return
    arr = []
    store_inorder(root, arr)
    # Sort arr
    arr.sort()
    # Replave val from arr to tree
    replace_val_from_arr_to_tree(arr, root)


root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.right.right = Node(5)

traverse_inorder(root)
print '\n'
binary_tree_to_bst(root)
traverse_inorder(root)
