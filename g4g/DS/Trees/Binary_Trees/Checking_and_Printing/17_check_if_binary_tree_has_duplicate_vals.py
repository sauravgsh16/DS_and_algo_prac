''' Check binary tree has duplicates '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_dup(root, s):
    if not root:
        return False
    
    if root.val in s:
        return True
    
    s.add(root.val)
    return check_dup(root.left, s) or check_dup(root.right, s)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(6)

s = set()
print check_dup(root, s)