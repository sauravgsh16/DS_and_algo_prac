''' Reverse level order traversal '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    


def reverse_level_order_traversal(root):
    if not root:
        return
    q = []
    s = []

    q.append(root)
    while len(q) > 0:
        node = q.pop(0)
        s.append(node)
        # NEED TO ENQUEUE RIGHT CHILD FIRST
        if node.right is not None:
            q.append(node.right)
        
        if node.left is not None:
            q.append(node.left)
    
    while len(s) > 0:
        print s.pop().val,

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

reverse_level_order_traversal(root)