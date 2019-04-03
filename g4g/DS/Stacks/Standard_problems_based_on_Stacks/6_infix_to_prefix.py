''' Convert Infix to Prefix '''
'''
   1) Reverse the infix expression.
      **** NOTE : '(' will become ')' and ')' becomes '('
   2) Obtain postfix expression reversed expression
   3) Reverse the postfix to obtain infix 
'''

class Conversion(object):

    def __init__(self, exp):
        self.exp = exp
        self.stack = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0
    
    def reverse(self, exp):
        ''' Conversion of brackets also considered '''
        new_exp = exp[::-1]
        for i in range(len(new_exp)):
            if new_exp[i] == '(':
                new_exp = new_exp[:i] + ')' + new_exp[i+1:]
            elif new_exp[i] == ')':
                new_exp = new_exp[:i] + '(' + new_exp[i+1:]
        return new_exp

    def peek(self):
        return self.stack[-1]

    def isOperand(self, ch):
        return ch.isalpha()

    def notGreater(self, op):
        a = self.precedence.get(op)
        b = self.precedence.get(self.peek())
        if a is None or b is None:
            return False
        return True if a <= b else False

    def infix_to_postfix(self):
        output = ''
        new_exp = self.reverse(self.exp)
        for i in new_exp:
            if self.isOperand(i):
                output += i
            elif i == '(':
                self.push(i)
            elif i == ')':
                while not self.isEmpty() and self.peek() != '(':
                    output += self.pop()
                if not self.isEmpty() and self.peek() != '(':
                    return -1
                self.pop()
            else:
                while not self.isEmpty() and self.notGreater(i):
                    output += self.pop()
                self.push(i)
        while not self.isEmpty():
            output += self.pop()
        return output

    def infix_to_prefix(self):
        post = self.infix_to_postfix()
        return self.reverse(post)


exp = '(a-b/c)*(a/k-l)'
c = Conversion(exp)
print c.infix_to_prefix()