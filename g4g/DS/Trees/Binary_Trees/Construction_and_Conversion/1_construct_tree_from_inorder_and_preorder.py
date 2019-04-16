''' Construct a tree from given inorder and preorder traversals '''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

pre_index = 0
def construct_tree(inorder, preorder):
    global pre_index
    if pre_index >= len(preorder) or not inorder:
        return
    inorder_index = inorder.index(preorder[pre_index])
    root = inorder[inorder_index]
    pre_index += 1
    
    left_inorder = inorder[:inorder_index]
    right_inorder = inorder[inorder_index+1:]
    node = Node(root)
    node.left = construct_tree(left_inorder, preorder)
    node.right = construct_tree(right_inorder, preorder)
    return node

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.val,
    inorder(root.right)


inOrder = [4, 2, 5, 1, 3]
preOrder = [1, 2, 4, 5, 3]
root = construct_tree(inOrder, preOrder)
inorder(root)