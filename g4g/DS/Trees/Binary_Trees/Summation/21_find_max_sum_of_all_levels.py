''' Find maximum level sum in Binary Tree '''
import sys

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def max_level_sum(root):
    if not root:
        return 0
    
    q = []
    q.append(root)
    max_sum = -sys.maxsize

    while len(q) > 0:
        size = len(q)
        cur_sum = 0
        while size > 0:
            node = q.pop(0)
            cur_sum += node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            size -= 1
        if max_sum < cur_sum:
            max_sum = cur_sum
    
    return max_sum


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left  = Node(6)
root.right.right.right  = Node(7)

print max_level_sum(root)
