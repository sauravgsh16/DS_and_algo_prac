''' Iterative post order traversal with one stack '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None

def postorder_traversal(root):
    if root is None:
        return

    stack = []
    ans = []
    while True:
        while root:
            # Push root's right child and then root to stack
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
            root = root.left
        root = stack.pop()

        # If popped item has right child and the right child is not processed yet,
        # make sure right child is processed before root.
        if root.right is not None and peek(stack) == root.right:
            stack.pop() # Remove right child from stack
            stack.append(root) # Push root back to stack
            root = root.right
        else:
            ans.append(root.val)
            root = None
        if len(stack) <= 0:
            break
    print ans


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

postorder_traversal(root)