''' Check if a tree is continous '''

class Node(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_continuous(root):
    if not root:
        return
    
    if not root.left and not root.right:
        return True
    
    if not root.left:
        return abs(root.val - root.right.val) == 1 and check_continuous(root.right)
    
    if not root.right:
        return abs(root.val - root.left.val) == 1 and check_continuous(root.left)
    
    return abs(root.val - root.right.val) == 1 and \
        abs(root.val - root.left.val) == 1 and \
        check_continuous(root.left) and check_continuous(root.right)


root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(5)

print check_continuous(root)
