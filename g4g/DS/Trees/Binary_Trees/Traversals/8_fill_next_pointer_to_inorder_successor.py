'''
   Populate Inorder Successor for all nodes
   Given a Binary Tree where each node has following structure,
   write a function to populate next pointer for all nodes.
   The next pointer for every node should be set to point to inorder successor
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


def populate_next_pointer(root):
    if not root:
        return
    # Reverse recursive inorder traversal
    populate_next_pointer(root.right)
    root.next = populate_next_pointer.next
    populate_next_pointer.next = root
    populate_next_pointer(root.left)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
populate_next_pointer.next = None
populate_next_pointer(root)

ptr = root.left.left
while ptr:
    print ptr.val,
    ptr = ptr.next