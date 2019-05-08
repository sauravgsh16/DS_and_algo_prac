''' Iterative search BST '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def iterative_search(root, key):
    if not root:
        return -1
    
    cur = root
    while cur != None:
        if cur.val == key:
            return True
        
        elif cur.val > key:
            cur = cur.left
        else:
            cur = cur.right
    return False

root = Node(5)
root.left = Node(2)
root.right = Node(12)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(9)
root.right.right = Node(21)
root.right.right.left = Node(19)
root.right.right.right = Node(25)

print iterative_search(root, 25)
print iterative_search(root, 3)
print iterative_search(root, 30)