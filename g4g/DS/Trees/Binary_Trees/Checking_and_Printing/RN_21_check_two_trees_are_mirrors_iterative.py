''' Check if two trees are mirrors - Iterative '''

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

    s1 = []
    s2 = []
    while True:
        while t1 and t2:
            if t1.val != t2.val:
                return False
            s1.append(t1)
            s2.append(t2)
            t1 = t1.left
            t2 = t2.right
        if not (t1 == None and t2 == None):
            return False
        
        if len(s1) > 0 and len(s2) > 0:
            t1 = s1.pop()
            t2 = s2.pop()

            t1 = t1.right
            t2 = t2.left
        else:
            break
    return True

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