''' Check if each internal node has only one child '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# In Preorder traversal, descendants (or Preorder successors) of every node
# appear after the node. In the above example, 20 is the first node in preorder
# and all descendants of 20 appear after it. All descendants of 20 are smaller
# than it. For 10, all descendants are greater than it. In general, we can say,
# if all internal nodes have only one child in a BST, then all the descendants 
# of every node are either smaller or larger than the node. The reason is simple,
# since the tree is BST and every node has only one child,
# all descendants of a node will either be on left side or right side,
# means all descendants will either be smaller or greater.


def has_only_one_child(pre):
    INT_MIN = -2**32
    INT_MAX = 2**32
    prev = pre[0]
    for i in range(1, len(pre)-1):
        ele = pre[i]
        if ele <= INT_MAX and ele >= INT_MIN:
            if ele < prev:
                INT_MAX = prev - 1
            else:
                INT_MIN = prev + 1
            prev = ele
        else:
            return False
    return True


# Other solutions
# 1) preorder = reverse (postorder) only if nodes contain one child

pre = [8, 3, 5, 7, 6]
print has_only_one_child(pre)
