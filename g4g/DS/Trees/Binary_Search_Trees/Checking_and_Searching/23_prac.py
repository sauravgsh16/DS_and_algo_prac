class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


INT_MIN = -2**32
INT_MAX = 2**32


# return val : [cur_size, max, min, True/False, size]

def largest_bst(root):
    if not root:
        return 0, INT_MIN, INT_MAX, False, 0
    if root.left is None and root.right is None:
        return 1, root.val, root.val, True, 1

    ls = largest_bst(root.left)
    rs = largest_bst(root.right)

    ret = [0, 0, 0, 0, 0]
    # Calculate current size
    ret[0] = 1 + ls[0] + rs[0]

    # Check return val and check min-max
    if ls[3] and rs[3] and ls[1] < root.val and rs[2] > root.val:
        # Update max
        ret[1] = max(rs[1], max(ls[1], root.val))
        # Update min
        ret[2] = min(ls[2], min(rs[2], root.val))

        # Update whole size
        ret[4] = ret[0]
        ret[3] = True
        return ret

    # If not BST
    ret[4] = max(ls[4], rs[4])
    ret[3] = False
    return ret


root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(8)
root.right = Node(4)


print largest_bst(root)[4]
