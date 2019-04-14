''' Morris travesal '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def morris_traversal(root):
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
                pre.right = current
                current = current.left
            else:
                pre.right = None
                print current.val,
                current = current.right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

morris_traversal(root)