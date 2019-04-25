''' Sum of nodes at maximum depth of a Binary Tree '''

# Calculate the max depth of the tree
# Traverse the tree again, passing in the max-depth, recursively decrementing it.
# When max-depth == 1, add the value of the node to the sum

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def max_depth(node):
    if not node:
        return 0
    
    return 1 + max(max_depth(node.left), max_depth(node.right))


def sum_nodes_max_depth_util(node, total, depth):
    if depth == 0 or not node:
        return 0
    if depth == 1:
        total[0] += node.val
    sum_nodes_max_depth_util(node.left, total, depth-1)
    sum_nodes_max_depth_util(node.right, total, depth-1)


def sum_nodes_max_depth(root):
    depth = max_depth(root)
    total = [0]
    sum_nodes_max_depth_util(root, total, depth)
    return total[0]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print sum_nodes_max_depth(root)
