''' Inorder traversal using stacks '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    current = root
    stack = []
    done = 0

    while not done:
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            if len(stack) > 0:
                current = stack.pop()
                print current.val,
                current = current.right
            else:
                done = 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder(root)