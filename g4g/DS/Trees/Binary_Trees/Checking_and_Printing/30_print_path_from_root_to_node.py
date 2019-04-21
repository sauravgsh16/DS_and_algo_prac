''' Print path from root to node '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def has_path(root, node, arr):
    if not root:
        return False
    arr.append(root.val)
    if root.val == node:
        return True
    if (has_path(root.left, node, arr) or
        has_path(root.right, node, arr)):
        return True
    arr.pop()
    return False


def print_path(root, node):
    arr = []
    if has_path(root, node, arr):
        for i in arr:
            print i,

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(15)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

print_path(root, 15)