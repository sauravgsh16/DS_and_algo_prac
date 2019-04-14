''' Construction of an Expression Tree '''

'''
   Inorder traversal of expression tree produces infix version of given 
   postfix expression (same with preorder traversal it gives prefix expression)
'''

class ExpressionTree(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_operand(ch):
    return ch.isalpha()


def construct_tree(postfix):
    stack = []

    for char in postfix:
        if is_operand(char):
            exp = ExpressionTree(char)
            stack.append(exp)
        else:
            exp = ExpressionTree(char)
            t1 = stack.pop()
            t2 = stack.pop()
            exp.left = t2
            exp.right = t1
            stack.append(exp)
    
    return stack.pop()

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.val,
    inorder(root.right)


postfix = "ab+ef*g*-"
root = construct_tree(postfix)
inorder(root)
