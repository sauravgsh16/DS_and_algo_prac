''' Check whether a Binary Tree is Complete '''
'''
   A binary tree is complete if all the levels, except possibly the last, is
   completely filled and all the nodes are as far left as possible.
'''

class Node(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_binary_tree_complete(root):
    if not root:
        return
    
    queue = []
    queue.append(root)

    non_full = False

    while len(queue) > 0:
        node = queue.pop(0)
        # Check if left child is present
        if node.left:
            # If we have seen a non full node, and we see 
            # a node with non-empty left child, then the 
            # given tree is not a complete binary tree 
            if non_full == True:
                return False
            # Enqueue left child
            queue.append(node.left)
        # If this a non-full node, set the flag as true
        else:
            non_full = True
        
        if node.right:
            # If we have seen a non full node, and we  
            # see a node with non-empty right child, then 
            # the given tree is not a compelete BT
            if non_full == True:
                return False
            # Enqueue right child
            queue.append(node.right)
        # If this a non-full node, set the flag as true
        else:
            non_full = True
    
    return True
""" 
   Let us construct the following Binary Tree which 
   is not a complete Binary Tree 
            1 
          /   \ 
         2     3 
        / \     \ 
       4   5     6 
"""
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.right = Node(6)

if (check_binary_tree_complete(root)): 
    print "Complete Binary Tree"
else: 
    print "NOT a Complete Binary Tree"