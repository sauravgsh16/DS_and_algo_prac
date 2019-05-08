''' Second largest in a binary search tree '''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def second_largest(root):
    count = [0]
    second_largest_util(root, count)


def second_largest_util(root, count):
    if not root or count[0] >= 2:
        return
    second_largest_util(root.right, count)

    count[0] += 1
    if count[0] == 2:
        print root.val
        return
    second_largest_util(root.left, count)


root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(10)

second_largest(root)