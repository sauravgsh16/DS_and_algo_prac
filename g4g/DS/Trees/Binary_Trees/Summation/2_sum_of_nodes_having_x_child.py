''' Sum of all nodes having child node 'x' '''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_sum_util(node, total, x):
    if not node:
        return 0
    if node.left and node.left.val == x or \
        node.right and node.right.val == x:
        total[0] += node.val
    find_sum_util(node.left, total, x)
    find_sum_util(node.right, total, x)

def find_sum(node, x):
    total = [0]
    find_sum_util(node, total, x)
    print total[0]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node('A')
root.right.left = Node('A')
root.right.right = Node(7)

find_sum(root, 'A')