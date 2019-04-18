''' Prefect Tree '''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_depth(node):
    d = 0
    while node != None:
        d += 1
        node = node.left
    return d

def is_perfect_util(root, d, level=0):
    if not root:
        return True
    
    if root.left is None and root.right is None:
        return d == level + 1
    return is_perfect_util(root.left, d, level+1) and \
        is_perfect_util(root.right, d, level + 1)

def is_tree_perfect(root):
    depth = get_depth(root)
    return is_perfect_util(root, depth)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print is_tree_perfect(root)