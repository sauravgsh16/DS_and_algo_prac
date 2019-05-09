''' Remove keys from BST outside a given range '''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def remove_nodes(root, min_r, max_r):
    if not root:
        return None

    root.left = remove_nodes(root.left, min_r, max_r)
    root.right = remove_nodes(root.right, min_r, max_r)

    if root.val < min_r:
        rChild = root.right
        return rChild

    if root.val > max_r:
        lChild = root.left
        return lChild

    return root


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.val,
    inorder(root.right)


root = Node(6)
root.left = Node(-13)
root.right = Node(14)
root.left.right = Node(-8)
root.right.left = Node(13)
root.right.left.left = Node(7)
root.right.right = Node(15)

inorder(root)
min_r, max_r = -10, 13
remove_nodes(root, min_r, max_r)

print '\n'
inorder(root)
