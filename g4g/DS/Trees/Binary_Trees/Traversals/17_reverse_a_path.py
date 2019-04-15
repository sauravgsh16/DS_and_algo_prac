''' Reverse a path of a binary tree '''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

nextpos = 0
def reverse_path_util(root, data, temp, level):
    global nextpos
    if not root:
        return
    
    if root.val == data:
        temp[level] = root.val
        root.val = temp[nextpos]
        nextpos += 1
        return root
    
    temp[level] = root.val

    # We want to go to the right only when we know that
    # data is not present in the right
    left = reverse_path_util(root.left, data, temp, level+1)
    if not left:
        right = reverse_path_util(root.right, data, temp, level+1)
    
    if left or right:
        root.val = temp[nextpos]
        nextpos += 1
        return left if left else right
    
    # Return None is data not found
    return None


def reverse_path(root, data):
    level = 0
    temp = [None] * 5  # Size of the tree
    reverse_path_util(root, data, temp, level)

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.val,
    inorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder(root)
print '\n'
reverse_path(root, 4)
inorder(root)