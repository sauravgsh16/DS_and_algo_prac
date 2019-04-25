''' Sum of heights of all individual nodes in a binary tree '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Compute max height of a node
def get_height(node):
    if not node:
        return 0
    
    l_height = get_height(node.left)
    r_height = get_height(node.right)

    if l_height > r_height:
        return l_height + 1
    else:
        return r_height + 1


def get_total_height(root):
    if not root:
        return 0
    
    return get_total_height(root.left) + get_height(root) + get_total_height(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print get_total_height(root)