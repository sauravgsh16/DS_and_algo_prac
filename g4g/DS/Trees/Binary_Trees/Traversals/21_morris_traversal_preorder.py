''' Morris traversal for preorder '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def morris_traversal_preorder(root):
    if not root:
        return
    
    current = root

    while current is not None:
        if not current.left:
            print current.val,
            current = current.right
        else:
            pre = current.left
            while pre.right is not None and pre.right != current:
                pre = pre.right
            
            if pre.right is None:
                print current.val, # PRINT STATEMENT HERE
                pre.right = current
                current = current.left
            else:
                pre.right = None
                current = current.right


def standard_preorder(root):
    if not root:
        return
    print root.val,
    standard_preorder(root.left)
    standard_preorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

standard_preorder(root)
print '\n'
morris_traversal_preorder(root)