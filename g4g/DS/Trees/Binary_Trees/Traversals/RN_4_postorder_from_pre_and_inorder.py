''' Postorder from Preorder and inorder '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def post_order_traversal(inorder, preorder, n):
    if preorder[0] in inorder:
        root = inorder.index(preorder[0])
    
    if root != 0: # Left subtree exists
        post_order_traversal(inorder[:root],
                             preorder[1:root+1],
                            len(inorder[:root]))
    if root != n - 1: # Right subtree exists
        post_order_traversal(inorder[root + 1:],
                             preorder[root + 1:],
                             len(inorder[root + 1:]))
    print preorder[0]


post_order_traversal([4, 2, 5, 1, 3, 6], [1, 2, 4, 5, 3, 6], 6)