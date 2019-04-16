''' Iterative postorder traversal with 2 stacks '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def postorder_traversal(root):
    if not root:
        return
    
    s1 = []
    s2 = []

    s1.append(root)
    while len(s1) > 0:
        node = s1.pop()
        s2.append(node)

        if node.left is not None:
            s1.append(node.left)
        if node.right is not None:
            s1.append(node.right)
    
    while len(s2) > 0:
        node = s2.pop()
        print node.val,


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

postorder_traversal(root)