''' Diagonal traversal of a Binary tree '''

# We use a map.
# We use the slope as the key. This mean, every time we travel to left of a
# node, a the slope will be incremented.

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def diagonal_traversal(root):
    diagonalMap = {}
    slope = 0

    def diagonal_traversal_util(root, slope):
        if not root:
            return
        try:
            diagonalMap[slope].append(root.val)
        except KeyError:
            diagonalMap[slope] = [root.val]
        
        # Since we are now traversing the left child, we increment the slope
        diagonal_traversal_util(root.left, slope+1)
        # The right child traversal will have the same slope
        diagonal_traversal_util(root.right, slope)
    
    diagonal_traversal_util(root, slope)
    for _, val in diagonalMap.iteritems():
        for v in val:
            print v,
        print '\n'


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.right.left = Node(6)
root.right.right = Node(14)
root.right.left.left = Node(4)
root.right.left.right = Node(7)
root.right.right.left = Node(13)

diagonal_traversal(root)

