''' Find node with minimum value '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_min(root):
    if not root:
        return -1
    cur = root
    while cur.left is not None:
        cur = cur.left
    return cur.val

root = Node(3)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(4)

print find_min(root)