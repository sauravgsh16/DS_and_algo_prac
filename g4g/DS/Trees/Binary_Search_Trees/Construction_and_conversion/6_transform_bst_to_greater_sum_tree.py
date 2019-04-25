''' BST to Greater sum Tree '''

'''
   Method 2
   By leveraging the fact that the tree is a BST, we can find an O(n) solution.
   The idea is to traverse BST in reverse inorder. Reverse inorder traversal
   of a BST gives us keys in decreasing order. Before visiting a node,
   we visit all greater nodes of that node. While traversing we keep track of
   sum of keys which is the sum of all the keys greater than the key of current node.
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def transform_bst_to_greater_sum_tree(root):
    tree_sum = [0]
    transform_bst_to_greater_sum_tree_util(root, tree_sum)


def transform_bst_to_greater_sum_tree_util(root, tree_sum):
    if not root:
        return

    transform_bst_to_greater_sum_tree_util(root.right, tree_sum)
    tree_sum[0] += root.val
    root.val = tree_sum[0] - root.val
    transform_bst_to_greater_sum_tree_util(root.left, tree_sum)


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.val,
    inorder(root.right)


root = Node(11)
root.left = Node(2)
root.right = Node(29)
root.left.left = Node(1)
root.left.right = Node(7)
root.right.left = Node(15)
root.right.right = Node(40)
root.right.right.left = Node(35)

transform_bst_to_greater_sum_tree(root)
inorder(root)
