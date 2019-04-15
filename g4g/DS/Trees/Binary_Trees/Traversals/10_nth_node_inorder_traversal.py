''' nth node of inorder traversal '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

count = 0
def nth_inorder(root, n):
    global count
    if not root:
        return
    if count < n:
        nth_inorder(root.left, n)
        count += 1
        if count == n:
            print root.val
            return
        nth_inorder(root.right, n)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
nth_inorder(root, 3)