''' Foldable binary tree '''

'''
   A tree can be folded if left and right subtrees are structure wise 
   mirror image of each other.

   isFoldable()
   -Algo: 
        1) If tree is empty, return True
        2) Convert the left subtree to its mirror image
        3) Check if the structure of left subtree and right subtree is same
           and store the result.
           res = isStructSame(root.left, root.right)  Recursive call
        4) Revert the changes in step 2, to get the original tree
        5) Return res.
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_foldable(root):
    if not root:
        return True
    mirror(root.left)
    res = is_struct_same(root.left, root.right)
    mirror(root.left)
    return res

def is_struct_same(a, b):
    if not a and not b:
        return True
    if a and b and is_struct_same(a.left, b.left) and is_struct_same(a.right, b.right):
        return True
    return False

def mirror(node):
    if not node:
        return
    mirror(node.left)
    mirror(node.right)
    temp = node.left
    node.left = node.right
    node.right = temp

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(6)

    print is_foldable(root)


main()
