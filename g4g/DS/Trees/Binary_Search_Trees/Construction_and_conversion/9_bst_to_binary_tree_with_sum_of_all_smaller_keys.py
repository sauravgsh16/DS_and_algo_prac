''' BST to a Tree with sum of all smaller keys '''
'''
  Input: Root of following BST
              5
            /   \
           2     13

   Output: The given BST is converted to following Binary Tree
              7
            /   \
          2      20
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
    bst_to_binary_tree_util(root.left, total)
    total[0] += root.val
    root.val = total[0]
    bst_to_binary_tree_util(root.right, total)


def preorder(root):
    if not root:
        return
    print root.val,
    preorder(root.left)
    preorder(root.right)


root = Node(9)
root.left = Node(6)
root.right = Node(15)
root.left.left = Node(3)
root.right.right = Node(21)


bst_to_binary_tree(root)
preorder(root)
