''' Check if BST contains dead ends '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_dead_ends(root, minm, maxm):
    if not root:
        return False
    
    if minm == maxm:
        return True

    return check_dead_ends(root.left, minm, root.val-1) or \
        check_dead_ends(root.right, root.val+1, maxm)


root1 = Node(4)
root1.left = Node(2)
root1.right = Node(7)
root1.left.left = Node(1)
root1.left.right = Node(3)
root1.right.left = Node(6)
root1.right.right = Node(10)

root2 = Node(10)
root2.left = Node(6)
root2.right = Node(20)
root2.left.left = Node(3)
root2.left.right = Node(7)


print check_dead_ends(root1, 1, 2**32)
print check_dead_ends(root2, 1, 2**32)