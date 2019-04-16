''' Construct Binary Tree from Inorder and Level Order Traversal '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def construct_tree(inorder, levelorder):
    if not inorder:
        return
    for i in range(len(levelorder)):
        if levelorder[i] in inorder:
            node = Node(levelorder[i])
            ino_index = inorder.index(levelorder[i])
            break
    print inorder[:ino_index], inorder[ino_index+1:]
    node.left = construct_tree(inorder[:ino_index], levelorder)
    node.right = construct_tree(inorder[ino_index+1:], levelorder)
    return node

def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print root.val,
    inorder_traversal(root.right)


levelorder = [20, 8, 22, 4, 12, 10, 14]
inorder = [4, 8, 10, 12, 14, 20, 22]
  

root = construct_tree(inorder, levelorder)
inorder_traversal(root)