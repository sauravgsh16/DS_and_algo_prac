''' Largest subtree sum in a tree '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def subtree_sum_util(node, max_sum):
    if not node:
        return 0
    
    cur_sum = node.val + subtree_sum_util(node.left, max_sum) +\
        subtree_sum_util(node.right, max_sum)
    
    max_sum[0] = max(max_sum[0], cur_sum)

    return cur_sum

def find_largest_subtree_sum(root):
    if not root:
        return 0
    
    max_sum = [0]
    subtree_sum_util(root, max_sum)
    return max_sum[0]


root = Node(1)
root.left = Node(-2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(-6)
root.right.right = Node(2)

print find_largest_subtree_sum(root)
