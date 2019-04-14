''' Evaluation of an Expression tree '''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def evaluate_expression_tree(root):
    if not root:
        return

    if root.left is None and root.right is None:
        return int(root.val)

    left_sum = evaluate_expression_tree(root.left)
    right_sum = evaluate_expression_tree(root.right)

    if root.val == '+':
        return left_sum + right_sum
    elif root.val == '-':
        return left_sum - right_sum
    elif root.val == '*':
        return left_sum * right_sum
    else:
        return left_sum / right_sum


root = Node('+') 
root.left = Node('*') 
root.left.left = Node('5') 
root.left.right = Node('4') 
root.right = Node('-') 
root.right.left = Node('100') 
root.right.right = Node('20') 

print evaluate_expression_tree(root)