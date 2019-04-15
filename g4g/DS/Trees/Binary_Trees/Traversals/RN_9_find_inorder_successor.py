''' Inorder Successor of a node in Binary Tree '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def leftMostNode(node):
    while node != None and node.left != None:
        node = node.left
    return node

def rightMostNode(node):
    while node != None and node.right != None:
        node = node.right
    return node

def findInorderRecursive(root, x):
    if not root:
        return None
    if root == x or findInorderRecursive(root.left, x) or\
                    findInorderRecursive(root.right, x):
        if findInorderRecursive(root.left, x):
            temp = findInorderRecursive(root.left, x)
        else:
            temp = findInorderRecursive(root.right, x)
        if temp:
            if root.left == temp:
                print 'Inorder successor', root.val
                return None
        return root
    return None

def inorder_successor(root, x):
    if x.right != None:
        inorderSucc = leftMostNode(x.right)
        print 'Inorder Successor', inorderSucc.val
    if x.right == None:
        rightMost = rightMostNode(root)
        if rightMost == x:
            print 'No successor'
        else:
            findInorderRecursive(root, x)


root = Node(1)  
root.left = Node(2)  
root.right = Node(3)  
root.left.left = Node(4)  
root.left.right = Node(5)  
root.right.right = Node(6)  

# Case 1  
inorder_successor(root, root.right)  

# case 2  
inorder_successor(root, root.left.left) 

# case 3  
inorder_successor(root, root.right.right)