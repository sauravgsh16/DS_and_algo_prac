''' Inorder successor in a BST '''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_successor(root, node):
    if node.right is not None:
        return get_minimim(root, node)

    succ = None
    while root is not None:
        if node.val < root.val:
            succ = root
            root = root.left
        elif node.val > root.val:
            root = root.right
        else:
            break
    return succ.val


def get_minimim(node):
    curr = node
    while curr is not None:
        if curr.left is None:
            break
        curr = curr.left
    return curr


root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)
root.left.left.left = Node(1)

print inorder_successor(root, root.left.left.left)
