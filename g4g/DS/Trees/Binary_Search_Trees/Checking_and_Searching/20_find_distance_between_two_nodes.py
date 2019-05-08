''' Find the distance between 2 nodes '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def distance_from_root(root, n):
    if root.val == n:
        return 0
    elif root.val > n:
        return 1 + distance_from_root(root.left, n)
    return 1 + distance_from_root(root.right, n)


def difference_2_nodes(root, a, b):
    if not root:
        return 0
    
    if root.val > a and root.val > b:
        return difference_2_nodes(root.left, a, b)
    
    if root.val < a and root.val < b:
        return difference_2_nodes(root.right, a, b)
    
    if root.val >= a and root.val <= b:
        return distance_from_root(root, a) + distance_from_root(root, b)


def find_dist_wrapper(root, a, b):
    if a > b:
        a, b = b, a
    return difference_2_nodes(root, a, b)

root = Node(5)
root.left = Node(2)
root.right = Node(12)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(9)
root.right.right = Node(21)
root.right.right.left = Node(19)
root.right.right.right = Node(25)

print find_dist_wrapper(root, 3, 12)
