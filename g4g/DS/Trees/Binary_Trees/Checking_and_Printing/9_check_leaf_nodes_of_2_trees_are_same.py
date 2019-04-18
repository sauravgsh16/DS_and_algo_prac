''' Check if the leaf nodes of 2 trees is the same '''

'''
   Constraint:
   Space : O(t1 + t2) - where t1 and t2 is the height of 2 trees
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and  self.right is None

def check_leaf_nodes(r1, r2):
    if not r1 and not r2:
        return
    
    s1 = []
    s2 = []
    s1.append(r1)
    s2.append(r2)

    while len(s1) > 0 or len(s2) > 0:
        if len(s1) == 0 or len(s2) == 0:
            return False
        
        node1 = s1.pop()
        node2 = s2.pop()
        while node1 is not None and not node1.is_leaf():
            if node1.right:
                s1.append(node1.right)
            if node1.left:
                s1.append(node1.left)
            node1 = s1.pop()
        
        while node2 is not None and not node2.is_leaf():
            if node2.right:
                s2.append(node2.right)
            if node2.left:
                s2.append(node2.left)
            node2 = s2.pop()
        
        if node2 is None and node1 is not None:
            return False
        if node1 is None and node2 is not None:
            return False
        
        if node2 is not None and node1 is not None:
            if node1.val != node2.val:
                return False

    return True

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

print check_leaf_nodes(root1, root2)