''' Check if a tree is a subtree of another tree '''

'''
   Method 1
   O(mn) solution , where m and n are heights of 2 trees ~ O(n^2)
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def are_trees_identical(t1, t2):
    if t1 is None and t2 is None:
        return True
    
    if t1 is None or t2 is None:
        return False
    
    return t1.val == t2.val and \
        are_trees_identical(t1.left, t2.left) and \
        are_trees_identical(t1.right, t2.right)


def is_subtree(t1, t2):
    if not t2:
        return True

    if not t1:
        return False

    if are_trees_identical(t1, t2):
        return True
    
    return is_subtree(t1.left, t2) or is_subtree(t1.right, t2)

'''
   METHOD 2:
   We use the inorder and preorder/postorder traversal of the trees.
   Since the inorder and preorder/postorder traversal of the subtree will
   be a subset of the inorder and preorder/postorder traversal of the main tree.

   Below, we use the combination of inorder and preorder
'''

def inorder_traversal(root, arr):
    if not root:
        return
    inorder_traversal(root.left, arr)
    arr.append(root.val)
    inorder_traversal(root.right, arr)


def preorder_traversal(root, arr):
    if not root:
        return
    arr.append(root.val)
    preorder_traversal(root.left, arr)
    preorder_traversal(root.right, arr)

def check_sub_arr(a1, a2):
    a1 = ''.join(str(i) for i in a1)
    a2 = ''.join(str(i) for i in a2)
    return a2 in a1

def check_subtree(t1, t2):
    if not t1:
        return False
    if not t2:
        return True
    in1 = []
    in2 = []
    pre1 = []
    pre2 = []
    
    inorder_traversal(t1, in1)
    inorder_traversal(t2, in2)
    preorder_traversal(t1, pre1)
    preorder_traversal(t2, pre2)

    return check_sub_arr(in1, in2) and check_sub_arr(pre1, pre2)


T1 = Node(1)
T1.left = Node(2)
T1.right = Node(3)
T1.left.left = Node(4)
T1.left.right = Node(5)
T1.right.left = Node(6)
T1.right.right = Node(7)

T2 = Node(3)
T2.left = Node(6)
T2.right = Node(7)

print is_subtree(T1, T2)
print check_subtree(T1, T2)
    