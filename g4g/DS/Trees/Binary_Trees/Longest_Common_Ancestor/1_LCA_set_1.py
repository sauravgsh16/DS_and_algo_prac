''' Longest Common Ancestor - Set 1 '''

'''
   Let T be a rooted tree, the lowest common ancestor between two nodes n1 and n2 is
   defined as the lowest node in T that has both n1 and n2 as descendants
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Method 1 - By storing root to n1 and root to n2 paths
# 1) Find path from root to n1 and store it in a vector
# 2) Find path from root to n2 and store it in a vector
# 3) Traverse both array, till value of arrays are the same.

def find_path(root, path, n):
    if not root:
        return False
    
    path.append(root.val)
    if root.val == n:
        return True
    
    if (root.left and find_path(root.left, path, n)) or \
        (root.right and find_path(root.right, path, n)):
        return True
    
    path.pop()
    return False


def find_LCA(root, n1, n2):
    path1 = []
    path2 = []

    if not find_path(root, path1, n1) or not find_path(root, path2, n2):
        return -1

    i = 0
    while len(path1) > i and len(path2) > i:
        if path1[i] != path2[i]:
            break
        i += 1
    
    return path1[i-1]


# Method 2
# Here we traverse the tree only once.
# We recursively check if any of the keys n1 or n2 matches the root, then root is LCA
# If not we recursively check in the left and right subtree
# IMPORTANT NOTE: We assume that both n1 and n2 are present in the tree

def find_LCA_alt(root, n1, n2):
    if not root:
        return
    
    if root.val == n1 or root.val == n2:
        return root
    
    left_lca = find_LCA_alt(root.left, n1, n2)
    right_lca = find_LCA_alt(root.right, n1, n2)

    if left_lca and right_lca:
        return root
    
    return left_lca if left_lca else right_lca


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print "LCA(4, 5) = %d" % find_LCA_alt(root, 4, 5,).val
print "LCA(4, 6) = %d" % find_LCA_alt(root, 4, 6).val
print "LCA(3, 4) = %d" % find_LCA_alt(root, 3, 4).val
print "LCA(2, 4) = %d" % find_LCA_alt(root, 2, 4).val
