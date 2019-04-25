''' Binary Search Tree '''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
        else:
            self._insert(self.root, node)

    def _insert(self, root, node):
        if not root:
            root = node
        else:
            if root.val < node.val:
                if root.right is None:
                    root.right = node
                else:
                    self._insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self._insert(root.left, node)


def search(key):
    node = search(root, key)
    if not node:
        return None
    return node.val


def _search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return _search(root.right, key)
    return _search(root.left, key)


def min_value_node(node):
    curr = node
    while curr.left is not None:
        curr = curr.left
    return curr


def delete_node(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)

    else:
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with 2 children: Get the inorder successor
        # (smallest in the right subtree)
        temp = min_value_node(root.right)
        # Copy the inorder's content to this node
        root.key = temp.key
        # Delete the inorder successor
        root.right = delete_node(root.right, temp.key)


def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print root.val,
    inorder(root.right)


bt = BinarySearchTree()
bt.insert(50)
bt.insert(30)
bt.insert(20)
bt.insert(40)
bt.insert(70)
bt.insert(60)
bt.insert(80)

inorder(bt.root)
print '\n'
bt.delete_node(20)
inorder(bt.root)
print '\n'
bt.delete_node(30)
inorder(bt.root)
print '\n'
bt.delete_node(50)
inorder(bt.root)
print '\n'
