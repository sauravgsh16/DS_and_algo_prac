''' Check if sum of all covered nodes is equal to uncovered nodes '''

'''
            9
        /       \
       4          17
    /    \         \
   3      6          22
        /   \        /
       5     7      20

    Unovered nodes: 9, 4, 3, 17, 22, 20
    Covered nodes:  6, 5, 7
'''

'''
   Need to get sum of uncovered nodes and subtract from sum of all nodes to get
   covered nodes
   Uncovered nodes: 
    1) traverse left, till none or right child
    2) traverse right, till none or left child
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sum_all_nodes(node):
    if not node:
        return 0
    return sum_all_nodes(node.left) + node.val +  sum_all_nodes(node.right)


def uncovered_sum_left(node):
    if node.left == None and node.right == None:
        return node.val
    
    if node.left is not None:
        return node.val + uncovered_sum_left(node.left)
    else:
        return node.val + uncovered_sum_left(node.right)

def uncovered_sum_right(node):
    if node.left == None and node.right == None:
        return node.val
    
    if node.right is not None:
        return node.val + uncovered_sum_left(node.right)
    else:
        return node.val + uncovered_sum_left(node.left)

def uncovered_sum(node):
    if not node:
        return
    
    left = right = 0
    if node.left:
        left = uncovered_sum_left(node.left)
    if node.right:
        right = uncovered_sum_right(node.right)
    
    return node.val + left + right


def check_sum(root):
    total = sum_all_nodes(root)
    uncovered = uncovered_sum(root)
    print total, uncovered

    return uncovered == (total - uncovered)


root = Node(9)
root.left = Node(4)
root.right = Node(17)
root.left.left = Node(3)
root.left.right = Node(6)
root.right.right = Node(22)
root.left.right.left = Node(5)
root.left.right.right = Node(7)
root.right.right.left = Node(20)

print check_sum(root)