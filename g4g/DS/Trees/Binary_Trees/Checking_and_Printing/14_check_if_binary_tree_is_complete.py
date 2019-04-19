''' Check if a binary tree is complete '''

'''
   A complete binary tree is a binary tree in which every level, except possibly
   the last, is completely filled, and all nodes are as far left as possible
   The following trees are examples of Complete Binary Trees
       1
     /   \
    2     3
  
          1
        /   \
       2     3
      /
     4

          1
        /    \
       2      3
     /  \    /
    4    5  6

    The following trees are examples of Non-Complete Binary Trees
    1
      \
       3
  
       1
    /    \
   2       3
    \     /  \   
     4   5    6

       1
    /    \
   2      3
         /  \
        4    5
'''
'''
   Solution:
   We can use level order traversal to check if tree is complete or not.
   We need to find the last full node. After that all nodes should be leaf nodes,
   if any of it are not a leaf node, then tree is not complete.

   We use a flag, which is initially set to False.
   If we don't find either left or right node, we set it to True.
   On next iteration, if we find either a left or right node, we check if flag
   is set to True, in that case we return False
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_tree_complete(root):
    if not root:
        return True
    
    q = []
    q.append(root)
    flag = False
    while len(q) > 0:
        node = q.pop(0)

        if node.left:
            q.append(node.left)
            if flag == True:
                return False
        else:
            flag = True
        
        if node.right:
            q.append(node.right)
            if flag == True:
                return False
        else:
            flag = True
    return True

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
# root.right.right = Node(7)

print is_tree_complete(root)
