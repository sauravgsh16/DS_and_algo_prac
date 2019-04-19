''' Check if the tree is a symmetric tree - Iterative '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def check_symmetric(root):
    if not root:
        return True
    
    if not root.left and not root.right:
        return True
    
    q = []

    # Append left and right, since we don't need to check root node
    q.append(root.left)
    q.append(root.right)

    while len(q) > 0:

        left_node = q.pop(0)
        right_node = q.pop(0)

        if left_node.val != right_node.val:
            return False
        
        if left_node.left and right_node.right:
            q.append(left_node.left)
            q.append(right_node.right)
        elif left_node.left or right_node.right:
            return False
        
        if left_node.right and right_node.left:
            q.append(left_node.right)
            q.append(right_node.left)
        elif left_node.right or right_node.left:
            return False
    
    return True, count

root = Node(1) 
root.left = Node(2) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(4) 
root.right.left = Node(4) 
root.right.right = Node(3)

print check_symmetric(root)
            