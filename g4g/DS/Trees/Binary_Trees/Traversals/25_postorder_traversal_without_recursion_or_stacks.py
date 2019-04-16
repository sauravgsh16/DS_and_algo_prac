''' Postorder traversal without recusion or stack '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Idea is keep track of all visited node in a hashmap
def postorder_traversal(root):
    visited = set()
    current = root

    # We travese one direction at a time,
    # Once we reach the end and know that there are no left and right child,
    # We print the node, add that node to the visited hash, and assign
    # current to be root node again.
    while current and current not in visited:
        if current.left and current.left not in visited:
            current = current.left
        elif current.right and current.right not in visited:
            current = current.right
        else:
            print current.val,
            visited.add(current)
            current = root

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.right.left = Node(6)
root.right.right = Node(14)
root.right.left.left = Node(4)
root.right.left.right = Node(7)
root.right.right.left = Node(13)


#postorder_traversal(root)
diagonalPrint(root)