''' Find middle of a perfect binary tree without finding height '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

'''
   Use two pointer slow and fast, like linked list
   Move fast by 2 leaf nodes, and slow by one.
   Once fast reaches leaf, print slow.
   Recursively call next route.
'''

def find_middle_util(slow, fast):
    # import pdb; pdb.set_trace()
    if slow is None or fast is None:
        return
    if fast.left is None and fast.right is None:
        print slow.val,

    find_middle_util(slow.left, fast.left.left)
    find_middle_util(slow.right, fast.left.left)


def find_middle(root):
    find_middle_util(root, root)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

find_middle(root)