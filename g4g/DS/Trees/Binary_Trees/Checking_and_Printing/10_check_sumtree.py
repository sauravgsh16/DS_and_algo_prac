''' Check sum tree '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_leaf(node):
    if not node:
        return False
    return node.left == None and node.right == None

def is_sum_tree(node):
    if not node or is_leaf(node):
        return True
    
    if is_sum_tree(node.left) and is_sum_tree(node.right):
        if not node.left:
            ls = 0
        elif is_leaf(node.left):
            ls = node.left.val
        else:
            ls = 2 * node.left.val
        
        if not node.right:
            rs = 0
        elif is_leaf(node.right):
            rs = node.right.val
        else:
            rs = 2 * node.right.val
        
        return node.val == ls + rs
    return False


# RECURSIVE

def subtree_sum(node):
    if not node:
        return 0
    return subtree_sum(node.left) + node.val + subtree_sum(node.right)


def is_sumtree_recursive(node):
    if not node or (node.left is None and node.right is None):
        return True
    
    ls = subtree_sum(node.left)
    rs = subtree_sum(node.right)

    return node.val == ls + rs and \
        is_sumtree_recursive(node.left) and \
        is_sumtree_recursive(node.right)