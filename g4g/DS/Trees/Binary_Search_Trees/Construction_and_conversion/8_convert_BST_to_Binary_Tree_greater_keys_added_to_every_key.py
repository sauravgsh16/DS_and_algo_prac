'''
   Convert a BST to a Binary Tree such that sum of all greater keys is added to
   every key

   Input: Root of following BST
              5
            /   \
           2     13

   Output: The given BST is converted to following Binary Tree
              18
            /   \
          20     13
'''

'''
   Solution:
   Traverse tree in reverse and add node values to present key.
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bst_to_binary_tree(root):
    total = [0]
    bst_to_binary_tree_util(root, total)


def bst_to_binary_tree_util(root, total):
    if not root:
        return
    bst_to_binary_tree_util(root.right, total)
    total[0] += root.val
    root.val = total[0]
    bst_to_binary_tree_util(root.left, total)


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.val,
    inorder(root.right)


root = Node(5)
root.left = Node(2)
root.right = Node(13)

bst_to_binary_tree(root)
inorder(root)
