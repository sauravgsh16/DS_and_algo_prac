''' Level ordre traversal '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_order_traversal(root):
    if not root:
        return
    
    q = []
    q.append(root)

    while len(q) > 0:
        node = q.pop(0)
        print node.val,

        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

level_order_traversal(root)