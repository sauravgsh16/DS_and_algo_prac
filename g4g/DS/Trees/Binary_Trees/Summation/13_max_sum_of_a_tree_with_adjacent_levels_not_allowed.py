''' Maximum sum from a tree with adjacent levels not allowed '''

'''
   Soln:
   Since adjacent levels are not allowed, we need to check maximum level of 
   the grandchildren starting at the root and the sum of grandchildren starting
   at level 2 
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def max_adjacent_sum(node):
    if not node:
        return 0
    
    sm = node.val
    if node.left:
        sm += get_sum(node.left.left)
        sm += get_sum(node.left.right)
    
    if node.right:
        sm += get_sum(node.right.left)
        sm += get_sum(node.right.right)

    return sm

def get_sum(node):
    if not node:
        return 0
    
    return max(max_adjacent_sum(node), 
               (max_adjacent_sum(node.left) + max_adjacent_sum(node.right)))


root = Node(1); 
root.left = Node(2); 
root.right = Node(3); 
root.right.left = Node(4); 
root.right.left.right = Node(5); 
root.right.left.right.left = Node(6);

print get_sum(root)
