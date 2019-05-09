''' Count the number of BST subtrees within a range '''

''' Count nodes within a range '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_bst_util(root, min_r, max_r, count):
    if not root:
        return True
    
    l = count_bst_util(root.left, min_r, max_r, count)
    r = count_bst_util(root.right, min_r, max_r, count)

    if l and r and root.val > min_r and root.val < max_r:
        count[0] += 1
        return True
    return False


def count_bst(root, min_r, max_r):
    count = [0]
    count_bst_util(root, min_r, max_r, count)
    return count[0]


root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)
root.left.left.left = Node(1)

min_r = 0
max_r = 10

print count_bst(root, min_r, max_r)