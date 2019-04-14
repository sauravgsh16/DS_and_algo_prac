''' Morris Inorder traversal '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def morris_inorder_traversal(root):
    current = root

    while current is not None:
        if current.left is None:
            print current.val,
            current = current.right
        else:
            pre = current.left

            # Find the right most node of pre such that
            # pre.right != current
            # when we find the right most node, we link it
            # to current, so that we have a way to reach current
            while pre.right is not None and pre.right != current:
                pre = pre.right
            
            if pre.right is None:
                # Linking pre right to current
                pre.right = current
                # Go to the left node
                current = current.left
            else:
                # We reach here when the left side has
                # already been processed, thus we need to remove
                # the link of pre.right to current
                pre.right = None
                print current.val,
                current = current.right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

morris_inorder_traversal(root)