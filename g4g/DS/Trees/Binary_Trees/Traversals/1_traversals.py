''' Inorder, preorder & postorder '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.val,
    inorder(root.right)


def preorder(root):
    if not root:
        return
    print root.val,
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print root.val,


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
print "Preorder traversal of binary tree is"
preorder(root) 
  
print "\nInorder traversal of binary tree is"
inorder(root) 
  
print "\nPostorder traversal of binary tree is"
postorder(root) 