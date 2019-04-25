''' Construct BST from preorder traversal - Set 1 (Recursive solutions)'''

'''
   r = 10
              10
    [5, 1, 7]    [40, 50]
        5            40
    [1]    [7]           [50]
'''




import sys
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# METHOD 1
def construct_binary_tree(preorder):
    ''' O(n^2) '''
    if not preorder:
        return None
    root = Node(preorder[0])
    if len(preorder) == 1:
        return root

    leftIndex = None
    for i in range(len(preorder)):
        if preorder[i] > root.val:
            leftIndex = i
            break
    # Left Subtree Construction
    root.left = construct_binary_tree(preorder[1: leftIndex])
    # Right Subtree construction
    root.right = construct_binary_tree(preorder[leftIndex:len(preorder)])
    return root


# METHOD 2
int_min = -sys.maxsize
int_max = sys.maxsize
index = 0


def get_index():
    return index


def increment_index():
    global index
    index += 1


def construct_binary_tree_method_2(pre):
    size = len(pre)
    return construct_tree_util(pre, pre[0], int_min, int_max, size)


def construct_tree_util(pre, key, int_min, int_max, size):
    if get_index() >= size:
        return None

    root = None

    if key > int_min and key < int_max:
        root = Node(key)
        increment_index()

        if get_index() < size:
            root.left = construct_tree_util(
                pre, pre[get_index()], int_min, key, size)

            root.right = construct_tree_util(
                pre, pre[get_index()], key, int_max, size)
    return root


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.val,
    inorder(root.right)


preorder = [10, 5, 1, 7, 40, 30, 50]
root1 = construct_binary_tree(preorder)
root2 = construct_binary_tree_method_2(preorder)
inorder(root1)
print '\n'
inorder(root2)
