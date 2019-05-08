''' Find kth largest element in BST using constant extra space '''

# Idea is to do reverse Morris Traversal

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def kth_largest(root, k):
    curr = root
    kth_largest = None

    count = 0

    while curr != None:
        if curr.right is None:

            count += 1
            if count == k:
                kth_largest = curr
            curr = curr.left
        else:
            succ = curr.right
            
            while succ.left != None and succ.left != curr:
                succ = succ.left
            
            if succ.left is None:
                succ.left = curr
                curr = curr.right

            else:
                succ.left = None
                count += 1
                if count == k:
                    kth_largest = curr
                curr = curr.left
    return kth_largest