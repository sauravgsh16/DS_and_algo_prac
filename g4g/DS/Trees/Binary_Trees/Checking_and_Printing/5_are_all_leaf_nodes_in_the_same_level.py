''' Check if all leaf nodes are at the same level '''
import sys


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# ITERATIVE

def check_leaf_level(root):
    if not root:
        return
    max_level = sys.maxsize
    level = 0

    q = []
    q.append(root)
    while len(q) > 0:
        size = len(q)
        level += 1

        while size > 0 or len(q):
            node = q.pop(0)
            if node.left:
                q.append(node.left)

                if not node.left.left and not node.left.right:
                    if max_level == sys.maxsize:
                        max_level = level
                    elif max_level != level:
                        return False
            
            if node.right:
                q.append(node.right)

                if not node.right.left and not node.right.right:
                    if max_level == sys.maxsize:
                        max_level = level
                    elif max_level != level:
                        return False
            size -= 1
        return True

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

print check_leaf_level(root)