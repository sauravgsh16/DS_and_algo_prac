''' Count subtrees that sum up to a given value x '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_subtree_util(node, count, x):
    if not node:
        return 0
    
    ls = count_subtree_util(node.left, count, x)
    rs = count_subtree_util(node.right, count, x)

    s = ls + rs + node.val
    if s == x:
        count[0] += 1
    return s


def count_subtree(root, x):
    if not root:
        return 0
    
    count = [0]
    ls = count_subtree_util(root.left, count, x)
    rs = count_subtree_util(root.right, count, x)

    if (ls + rs + root.val) == x:
        count[0] += 1
    return count[0]


root = Node(5)
root.left = Node(-10)
root.right = Node(3)
root.left.left = Node(9)
root.left.right = Node(8)
root.right.left = Node(-4)
root.right.right = Node(7)


print count_subtree(root, 7)