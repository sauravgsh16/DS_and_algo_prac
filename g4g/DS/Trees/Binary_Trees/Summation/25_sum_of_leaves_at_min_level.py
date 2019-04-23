''' Sum of all leaves at minimum level '''

# Idea is to traverse in level order.
# Once we encunter a leaf, in any level, we sum all the leaf nodes and stop traversal

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sum_min_level(root):
    if not root:
        return 0
    
    q = []
    q.append(root)
    min_sum = 0
    loop = True
    while loop:
        size = len(q)
        while size > 0:
            node = q.pop(0)

            if not node.left and not node.right:
                loop = False
                min_sum += node.val
            else:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            size -= 1
    return min_sum


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
root.right.left.right = Node(9)

print sum_min_level(root)