''' Iterative preorder traversal '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder_traversal(root):
    if not root:
        return
    
    stack = []
    q=stack.append(root)

    while len(stack) > 0:
        node = stack.pop()
        print node.val,
        
        # NOTE : NEED TO PUSH RIGHT CHILD FIRST
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

preorder_traversal(root)