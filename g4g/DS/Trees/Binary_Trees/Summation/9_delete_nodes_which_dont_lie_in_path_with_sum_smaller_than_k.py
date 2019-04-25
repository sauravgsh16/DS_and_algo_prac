''' Delete nodes which don't lie in any path with sum <= k '''

# METHOD 1
'''
   Idea is to traverse the tree and delete the nodes in bottom up manner.
   While traversing the tree, recursively calculate the sum of nodes from
   root to leaf node of each path.
   For each visited node, check the total against 'k'. If sum is less than 'k',
   delete the node and return to previous node.
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def delete_tree(node, k, Sum):
    if not node:
        return
    
    left_sum = [Sum[0] + node.val]
    right_sum = [left_sum[0]]

    node.left = delete_tree(node.left, k, left_sum)
    node.right = delete_tree(node.right, k, right_sum)

    Sum[0] = max(left_sum[0], right_sum[0])

    if Sum[0] < k:
        node = None
    return node


def prune_tree(root, k):
    Sum = [0]
    return delete_tree(root, k, Sum)


def print_tree(root):
    if not root:
        return
    print_tree(root.left)
    print root.val,
    print_tree(root.right)


k = 45
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(12)
root.right.right.left = Node(10)
root.right.right.left.right = Node(11)
root.left.left.right.left = Node(13)
root.left.left.right.right = Node(14)
root.left.left.right.right.left = Node(15)

print_tree(root)
print '\n'
prune_tree(root, k)
print_tree(root)