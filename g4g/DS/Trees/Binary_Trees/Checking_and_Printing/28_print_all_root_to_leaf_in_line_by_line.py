''' Print all paths '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_path(node, arr):
    if not node:
        return
    arr.append(node.val)
    if node.left is None and node.right is None:
        print ' '.join([str(i) for i in arr])
    print_path(node.left, arr)
    print_path(node.right, arr)
    arr.pop()


def print_all_path(root):
    arr = []
    print_path(root, arr)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(15)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

print_all_path(root)