''' Sum of all nodes in a binary tree '''

''' Print path from root to node '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_sum(root):
    if not root:
        return 0
    return root.val + find_sum(root.left) + find_sum(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print find_sum(root)