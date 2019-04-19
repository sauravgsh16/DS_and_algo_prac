''' Check is tree is full binary tree - Iterative '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_full(root):
    q = []
    q.append(root)

    while len(q) > 0:
        node = q.pop(0)

        if not node.left and node.right:
            return False
        if node.left and not node.right:
            return False
        if node.right and node.left:
            q.append(node.right)
            q.append(node.left)
    return True

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print check_full(root)
        