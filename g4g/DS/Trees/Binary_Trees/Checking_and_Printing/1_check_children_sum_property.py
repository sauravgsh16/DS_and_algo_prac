''' Check for children sum property in a Binary Tree '''

'''
   For every node, data value must be equal to sum of data values in
   left and right children.
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_children_sum(node):
    if not node or (not node.left and not node.right):
        return True
    
    left_val = right_val = 0

    if node.left:
        left_val = node.left.val
    
    if node.right:
        right_val = node.right.val
    
    if node.val == left_val + right_val and \
        check_children_sum(node.left) and \
        check_children_sum(node.right):
        return True
    return False


root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

print check_children_sum(root)
