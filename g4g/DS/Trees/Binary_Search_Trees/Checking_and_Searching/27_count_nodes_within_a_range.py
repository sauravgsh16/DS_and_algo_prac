''' Count nodes within a range '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def node_count_util(root, min_r, max_r, count):
    if not root:
        return
    
    if root.val == min_r and root.val == max_r:
        count[0] = 1
        return
    
    if root.val > min_r:
        node_count_util(root.left, min_r, max_r, count)
    
    if root.val > min_r and root.val < max_r:
        count[0] += 1
    
    if root.val < max_r:
        node_count_util(root.right, min_r, max_r, count)
    


def node_count(root, min_r, max_r,):
    count = [0]
    node_count_util(root, min_r, max_r, count)
    return count[0]


def node_count_alt(root, min_r, max_r):
    if not root:
        return 0

    if root.val == min_r and root.val == max_r:
        return 1
    
    if root.val > min_r and root.val < max_r:
        return 1 + node_count_alt(root.left, min_r, max_r) + \
            node_count_alt(root.right, min_r, max_r)
    
    if root.val > min_r:
        return node_count_alt(root.left, min_r, max_r)
    else:
        return node_count_alt(root.right, min_r, max_r)


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

print node_count(root, min_r, max_r)
print node_count_alt(root, min_r, max_r)