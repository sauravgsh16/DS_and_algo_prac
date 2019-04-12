''' Insertion into a binary tree '''


'''
   We traverse by level and the new node once we find a either an empty left
   child or right child.
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert_node(root, val):
    if root is None:
        return
    
    q = []
    q.append(root)

    while len(q) > 0:
        node = q.pop(0)

        if not node.left:
            node.left = Node(val)
            break
        else:
            q.append(node.left)
        if not node.right:
            node.right = Node(val)
            break
        else:
            q.append(node.right)


def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print root.val,
    inorder_traversal(root.right)


root = Node(10)
root.left = Node(11)
root.right = Node(9)
root.left.left = Node(7)
root.right.left = Node(15)
root.right.right = Node(8)

inorder_traversal(root)
insert_node(root, 12)
print '\n'
inorder_traversal(root)