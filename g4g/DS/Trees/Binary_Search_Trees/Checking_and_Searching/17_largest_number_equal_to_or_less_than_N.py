''' Find largest number equal to or less than N '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_max_for_N(root, n):
    if not root:
        return -1
    
    if root.val == n:
        return n
    
    elif root.val < n:
        k = find_max_for_N(root.right, n)
        if k == -1:
            return root.val
        else:
            return k
    elif root.val > n:
        return find_max_for_N(root.left, n)


root = Node(5)
root.left = Node(2)
root.right = Node(12)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(9)
root.right.right = Node(21)
root.right.right.left = Node(19)
root.right.right.right = Node(25)

print find_max_for_N(root, 24)