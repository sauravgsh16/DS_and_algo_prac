''' Find kth largest element in a BST '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# We just need to traverse inorder - BUT IN REVERSE ORDER

def kth_largest_element(root, k, count):
    if not root:
        return None
    
    kth_largest_element(root.right, k, count)
    count[0] += 1
    if count[0] == k:
        print root.val
        return
    kth_largest_element(root.left, k, count)


def print_kth_largest(root, k):
    count = [0]
    kth_largest_element(root, k, count)


root = Node(40)
root.left = Node(20)
root.right = Node(50)
root.left.left = Node(10)
root.left.right = Node(30)

print_kth_largest(root, 2)