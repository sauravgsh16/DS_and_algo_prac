''' Print key within range in constant space '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_values_morris_traversal(root, min_r, max_r):
    if not root:
        return
    
    curr = root
    while curr != None:
        if curr.left is None:
            if curr.val > min_r and curr.val < max_r:
                print curr.val,
            curr = curr.right
        else:
            pre = curr.left
            while pre.right is not None and pre.right != curr:
                pre = pre.right
            if pre.right is None:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                if curr.val > min_r and curr.val < max_r:
                    print curr.val,
                curr = curr.right


root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)
root.left.left.left = Node(1)

min_r = 2
max_r = 8

print_values_morris_traversal(root, min_r, max_r)
