''' Count the number of BST subtrees within a range '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def delete_leaf_nodes(root):
    if root.left == None and root.right == None:
        return None
    
    root.left = delete_leaf_nodes(root.left)
    root.right = delete_leaf_nodes(root.right)

    return root


def insert(root, val):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.val,
    inorder(root.right)


root = None
root = insert(root, 20)
insert(root, 10)
insert(root, 5)
insert(root, 15)
insert(root, 30)
insert(root, 25)
insert(root, 35)

inorder(root)
print '\n'
delete_leaf_nodes(root)
inorder(root)