''' Sum of all left leaf nodes '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isLeaf(node):
    if not node:
        return False
    return node.left is None and node.right is None

def sum_left_leaf(root):
    res = 0
    if root is not None:
        if isLeaf(root.left):
            res += root.left.val
        else:
            res += sum_left_leaf(root.left)
        res += sum_left_leaf(root.right)
    return res


root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.right.left = Node(23)
root.right.right = Node(52)
root.right.right.left = Node(50)
root.left.left = Node(5)
root.left.right = Node(12)
root.left.right.right = Node(12)

print sum_left_leaf(root)