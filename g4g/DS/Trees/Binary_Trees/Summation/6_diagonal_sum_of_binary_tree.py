''' Diagonal sum of binary tree '''

# We use a map.
# We use the slope as the key. This mean, every time we travel to left of a
# node, a the slope will be incremented.

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def diagonal_sum_util(root, slope, sum_dict):
    if not root:
        return
    try:
        sum_dict[slope] += root.val
    except KeyError:
        sum_dict[slope] = root.val
    
    diagonal_sum_util(root.left, slope+1, sum_dict)
    diagonal_sum_util(root.right, slope, sum_dict)


def diagonal_sum(root):
    sum_dict = {}
    slope = 0
    diagonal_sum_util(root, slope, sum_dict)
    for key, val in sum_dict.iteritems():
        print 'level', key, '->', val


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(9)
root.left.right = Node(6)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.left.right = Node(7)
root.right.left.left = Node(12)
root.left.right.left = Node(11)
root.left.left.right = Node(10)

diagonal_sum(root)