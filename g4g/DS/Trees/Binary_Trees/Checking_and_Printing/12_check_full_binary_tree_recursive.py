''' Check if binary tree is full '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_full(node):
    if not node:
        return True
    if not node.left and not node.right:
        return True

    if node.left is not None and node.right is not None:
        return check_full(node.left) and check_full(node.right)
    return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

print check_full(root)