'''
    Check if given tree is sum tree
          26
        /   \
      10     3
    /    \     \
  4      6      3
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# METHOD 1:
# Gets sum of nodes of left subtree and right subtree. Check if the sum
# calculated is equal to root's data. Also, recursively check if left and
# right subtrees are sum trees

# Time - O(n^2)

def subtree_sum(node):
    if not node:
        return 0
    return subtree_sum(node.left) + node.val + subtree_sum(node.right)

def is_sumtree(node):
    if not node or (not node.left and not node.right):
        return True
    
    ls = subtree_sum(node.left)
    rs = subtree_sum(node.right)

    if node.val == ls + rs and \
        is_sumtree(node.left) and \
        is_sumtree(node.right):
        return True
    return False

# **********************************************************

# METHOD 2- EFFICIENT
'''
   This method uses following rules to get the sum directly.
   1) If the node is a leaf node then sum of subtree rooted with this node
      is equal to value of this node.
   2) If the node is not a leaf node then sum of subtree rooted with this 
      node is twice the value of this node (Assuming that the tree rooted 
      with this node is SumTree).
'''

def is_leaf(node):
    if not node:
        return False
    if node.left == None and node.right == None:
        return True
    return False

def is_subtree_efficient(node):
    if not node or is_leaf(node):
        return True

    if is_subtree_efficient(node.left) and is_subtree_efficient(node.right):
        # Get sum of nodes in the left subtree
        if node.left == None:
            ls = 0
        elif is_leaf(node.left):
            ls = node.left.val
        else:
            ls = 2 * node.left.val
        # Get sum of node in the right subtree
        if node.right == None:
            rs = 0
        elif is_leaf(node.right):
            rs = node.right.val
        else:
            rs = 2 * node.right.val

        if node.val == rs + ls:
            return True
        return False
    return False

root = Node(26)
root.left = Node(10)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.right = Node(3)

print is_sumtree(root)
print is_subtree_efficient(root)
