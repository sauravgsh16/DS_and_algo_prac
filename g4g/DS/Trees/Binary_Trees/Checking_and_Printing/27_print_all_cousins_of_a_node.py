''' Print all cousins of a node '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_level(root, node, level):
    if not root:
        return 0
    if root == node:
        return level
    lvl = find_level(root.left, node, level + 1)
    if lvl != 0:
        return lvl
    return find_level(root.right, node, level + 1)


def print_siblings_util(root, node, level):
    if not root or level < 2:
        return
    if level == 2:
        if root.left == node or root.right == node:
            return
        if root.left:
            print root.left.val,
        if root.right:
            print root.right.val,
    elif level > 2:
        print_siblings_util(root.left, node, level -1)
        print_siblings_util(root.right, node, level - 1)


def print_siblings(root, node):
    level = find_level(root, node, 1)
    print print_siblings_util(root, node, level)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(15)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

print_siblings(root, root.left.right.right)