''' Lowest Common Ancestor in a Binary Search Tree '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lca_recursive(root, n1, n2):
    if not root:
        return
    
    if root.val > n1 and root.val > n2:
        return lca_recursive(root.left, n1, n2)
    
    if root.val < n1 and root.val < n2:
        return lca_recursive(root.right, n2, n1)
    
    return root.val


def lca_iterative(root, n1, n2):

    while root is not None:
        if root.val > n1 and root.val > n2:
            root = root.left
        
        elif root.val < n1 and root.val < n2:
            root = root.right
        else:
            break

    return root.val


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

n1 = 10
n2 = 14
print 'LCA of %d and %d is %s' % (n1, n2, lca_recursive(root, n1, n2))
print 'LCA of %d and %d is %s' % (n1, n2, lca_iterative(root, n1, n2))