''' Largest BST in a binary tree '''

# We use to property of a binary tree to solve this problem
# We traverse the tree in post order fashion and return the following
#   a. If the tree subtree is true
#   b. min value of subtree
#   c. max value of subtree
#   d. size of the tree


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


INT_MIN = -2**32
INT_MAX = 2**32

# Return val: [curr_size, max, min, True/False, whole_size]


def largest_BST(root):
    if root is None:
        return 0, INT_MIN, INT_MAX, True, 0
    if root.left is None and root.right is None:
        return 1, root.val, root.val, True, 1

    # Recur for the left subtree and right subtree
    ls = largest_BST(root.left)
    rs = largest_BST(root.right)

    ret = [0, 0, 0, 0, 0]
    # Set Size of tree
    ret[0] = 1 + ls[0] + rs[0]

    # Check if the subtrees are BST, checking the 4th val in the returned array
    # Also check if the current value is greater than min and less than max
    if ls[3] and rs[3] and ls[1] < root.val and rs[2] > root.val:
        # Set the min value for left
        ret[2] = max(rs[1], max(ls[1], root.val))
        # Set the max value for right
        ret[2] = min(ls[2], min(rs[1], root.val))

        # Update size for tree rooted under the current 'root'
        ret[4] = ret[0]
        ret[3] = True
        return ret

    # If whole subtree is not BST, return maximum size of left and right subtrees
    ret[4] = max(ls[4], rs[4])
    ret[3] = False
    return ret


root = Node(65)
root.left = Node(60)
root.right = Node(70)
#root.left.left = Node(50)


print largest_BST(root)[4]
