''' Convert a binary tree into a min heap - Using extra space'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_traversal(root, arr):
    if not root:
        return
    inorder_traversal(root.left, arr)
    arr.append(root.val)
    inorder_traversal(root.right, arr)


def get_inorder(root):
    arr = []
    inorder_traversal(root, arr)
    return arr


def level_order_convert(root, arr):
    if not root:
        return
    
    queue = []
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        node.val = arr.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def convert_binary_to_min_heap(root):
    inorder_arr = get_inorder(root)
    level_order_convert(root, inorder_arr)


root = Node(8)
root.left = Node(4)
root.right = Node(12)
root.left.left = Node(2)
root.left.right = Node(6)
root.right.left = Node(10)
root.right.right = Node(14)

convert_binary_to_min_heap(root)
print get_inorder(root)