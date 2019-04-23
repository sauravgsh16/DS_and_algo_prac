''' Sum of all leaf nodes '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sum_leaf_nodes_util(node, leaf_sum):
    if not node:
        return 0
    
    if not node.left and not node.right:
        leaf_sum[0] += node.val
    
    sum_leaf_nodes_util(node.left, leaf_sum)
    sum_leaf_nodes_util(node.right, leaf_sum)


def sum_leaf_nodes(root):
    leaf_sum = [0]
    sum_leaf_nodes_util(root, leaf_sum)
    return leaf_sum[0]

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.right = Node(7)
root.right.left = Node(6)
root.right.left.right = Node(8)

print sum_leaf_nodes(root)
