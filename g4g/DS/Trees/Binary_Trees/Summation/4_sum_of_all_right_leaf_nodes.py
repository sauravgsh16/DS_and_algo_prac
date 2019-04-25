''' Sum of all right leaf nodes '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sum_right(node, total):
    if not node:
        return 0    
    if node.right:
        if not node.right.left and not node.right.left:
            total[0] += node.right.val
    sum_right(node.left, total)
    sum_right(node.right, total)


def print_sum_right(node):
    total = [0]
    sum_right(node, total)
    print total[0]

root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.right.left = Node(23)
root.right.right = Node(52)
root.right.right.left = Node(50)
root.left.left = Node(5)
root.left.right = Node(12)
root.left.right.right = Node(12)

print_sum_right(root)