''' Construct BST from preorderorder - Set 2 (Iterative solution)'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def construct_binary_tree(preorder):
    if len(preorder) == 0:
        return
    if len(preorder) == 1:
        root = Node(preorder[0])
        return root

    stack = []
    root = Node(preorder[0])
    stack.append(root)

    import pdb
    pdb.set_trace()
    for i in range(1, len(preorder)):
        temp = None

        while len(stack) != 0 and preorder[i] > stack[-1].val:
            temp = stack.pop()

        if temp != None:
            temp.right = Node(preorder[i])
            stack.append(temp.right)
        else:
            temp = stack[-1]
            temp.left = Node(preorder[i])
            stack.append(temp.left)
    return root


def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print root.val,
    inorder(root.right)


preorder = [10, 5, 1, 7, 40, 50]
root = construct_binary_tree(preorder)
inorder(root)
