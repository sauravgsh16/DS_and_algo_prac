''' Construct a Full Binary Tree from Preorder and Postorder traversal '''

'''
   It is not possible to construct a general Binary Tree from preorder and
   postorder traversals.
   But if we know that the binary tree is 'FULL', we can construct the tree
   with ambiguity.

   Explanation:
   preorder = [1, 2, 4, 8, 9, 5, 3, 6, 7]
   postorder = [8, 9, 4, 5, 2, 6, 7, 3, 1]
   In 'pre', leftmost is root of tree. Since tree is Full and array size is more
   than 1, the value next to `1` in preorder, must be the left child of root.
   So - 1 is the root and 2 is the left child.
   To find all nodes of left subtree, we know 2 is the root node for left subtree,
   thus all node before 2 (8, 9, 4, 5)in postorder are in left subtree, and 
   elements (6, 7, 3) are in right subtree.
   We recursively follow the above approach to construct the tree.   
'''
pre =  [1, 2, 4, 8, 9, 5, 3, 6, 7]
post = [8, 9, 4, 5, 2, 6, 7, 3, 1]
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

pre_index = 0
def construct_tree(pre, post):
    global pre_index

    if pre_index >= len(pre) and not post:
        return
    root = Node(pre[pre_index])
    pre_index += 1


