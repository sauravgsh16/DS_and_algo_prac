''' Symmetric Tree '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_symmetric(root):
    return isMirror(root.left, root.right)


def isMirror(a, b):
    if a is None and b is None:
        return True
    
    if a and b:
        if a.val == b.val:
            return isMirror(a.left, b.right) and isMirror(a.right, b.left)
    return False



root = Node(1) 
root.left = Node(2) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(4) 
root.right.left = Node(4) 
root.right.right = Node(3)

print check_symmetric(root)