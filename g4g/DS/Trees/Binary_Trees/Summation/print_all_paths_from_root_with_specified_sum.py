''' Print all paths from the root with a specified sum '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_paths_util(node, specified_sum, cur_sum, path):
    if not node:
        return
    
    cur_sum += node.val
    path.append(node.val)

    if cur_sum == specified_sum:
        for i in range(len(path)):
            print path[i],
        print '\n'
    
    if node.left:
        print_paths_util(node.left, specified_sum, cur_sum, path)
    
    if node.right:
        print_paths_util(node.right, specified_sum, cur_sum, path)
    
    path.pop()


def print_paths(root, specified_sum):
    path = []
    print_paths_util(root, specified_sum, 0, path)


root = Node(10)
root.left = Node(28)
root.right = Node(13)
root.right.left = Node(14)
root.right.right = Node(15)
root.right.left.left = Node(21)
root.right.left.right = Node(22)
root.right.right.left = Node(23)
root.right.right.right = Node(24)

specified_sum = 38
print_paths(root, specified_sum)
