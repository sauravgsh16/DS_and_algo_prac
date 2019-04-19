''' Check if two trees are mirror '''

'''
   two trees 'a' and 'b' are mirrors
   1) Their root's key are the same
   2) a's left subtree is b's right subtree
   3) a's right subtree is b's left subtree
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_mirror(t1, t2):
    if not t1 and not t2:
        return True
    
    if not t1 or not t2:
        return False

    return t1.val == t2.val and \
        check_mirror(t1.left, t2.right) and \
        check_mirror(t1.right, t2.left)

r1 = Node(1)
r2 = Node(1)

r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)

r2.left = Node(3)
r2.right = Node(2)
r2.right.left = Node(5)
r2.right.right = Node(4)

print check_mirror(r1, r2)