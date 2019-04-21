''' Check if two nodes are cousins '''

'''
   Two nodes are cousins if they are in the same level
   but share different parents
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_level(root, node, lvl):
    if not root:
        return 0
    if root == node:
        return lvl
    level = find_level(root.left, node, lvl+1)
    if level:
        return level
    return find_level(root.right, node, lvl+1)


def is_sibling(root, node1, node2):
    if not root:
        return 0
    return (root.left == node1 and root.right == node2) or\
        (root.right == node1 and root.left == node2) or \
        is_sibling(root.left, node1, node2) or \
        is_sibling(root.right, node1, node2)

def check_cousins(root, node1, node2):
    level1 = find_level(root, node1, 1)
    level2 = find_level(root, node2, 1)

    return level1 == level2 and not is_sibling(root, node1, node2)


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.left.right.right = Node(15) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8)
  
node1 = root.left.right 
node2 = root.right.right  
  
print check_cousins(root, node1, node2)