''' Deletion in a binary tree '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def delete_node(root, key):
    if not root:
        return
    
    q = []
    q.append(root)

    while len(q) > 0:
        node = q.pop(0)

        if node.val == key:
            key_node = node
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    # Now node will contain the val of the deepest node
    replace_val = node.val
    delete_deepest_node(root, node)
    key_node.val = replace_val


def delete_deepest_node(root, d_node):
    if not root:
        return

    q = []
    q.append(root)

    while len(q) > 0:
        node = q.pop(0)
        if node.left:
            if node.left.val == d_node.val:
                node.left = None
                del(d_node)
                return
            else:
                q.append(node.left)
        if node.right:
            if node.right.val == d_node.val:
                node.right = None
                del(d_node)
                return
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
root.left.left = Node(7)
root.left.right = Node(12)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

inorder_traversal(root)
delete_node(root, 11)
print '\n'
inorder_traversal(root)