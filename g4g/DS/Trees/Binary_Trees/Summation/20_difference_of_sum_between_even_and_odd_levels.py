''' Difference between sums of odd level and even level nodes of a Binary Tree '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Idea is to do level order traversal

def diff_odd_even_levels(root):
    if not root:
        return 0
    
    q = []
    q.append(root)
    odd = even = level = 0
    while len(q) > 0:
        size = len(q)
        level += 1
        while size > 0:
            node = q.pop(0)
            if level % 2 == 0:
                even += node.val
            else:
                odd += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            size -= 1
    return odd - even

root = Node(5)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(4)
root.left.right.left = Node(3)
root.right.right = Node(8)
root.right.right.right = Node(9)
root.right.right.left = Node(7)

print diff_odd_even_levels(root)