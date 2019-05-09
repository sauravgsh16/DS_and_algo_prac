''' Print node values within a range in BST '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_values(root, min_r, max_r):
    if not root:
        return
    
    if root.val > min_r:
        print_values(root.left, min_r, max_r)
    
    if root.val > min_r and root.val < max_r:
        print root.val,
    
    if root.val < max_r:
        print_values(root.right, min_r, max_r)


root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)
root.left.left.left = Node(1)

min_r = 2
max_r = 8

print_values(root, min_r, max_r)