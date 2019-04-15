''' nth node of postorder traversal '''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

count = 0
def nth_postorder(root, n):
    global count
    if not root:
        return
    if count < n:
        nth_postorder(root.left, n)
        nth_postorder(root.right, n)
        count += 1
        if count == n:
            print root.val

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
nth_postorder(root, 3)