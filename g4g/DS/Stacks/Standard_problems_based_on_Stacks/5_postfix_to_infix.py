''' Convert Postfix to infix '''
'''
   Important points:
   1) Read from left to right
   2) Expression = ( OP2 + operation + OP1 )
'''

class Conversion(object):
    
    def __init__(self, exp):
        self.exp = exp
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        raise

    def isEmpty(self):
        return len(self.stack) == 0

    def isOperand(self, ch):
        return ch.isalpha()

    def postfix_to_infix(self):
        for i in self.exp:
            if self.isOperand(i):
                self.push(i)
            else:
                op1 = self.pop()
                op2 = self.pop()
                exp = '(' + op2 + i + op1 + ')'
                self.push(exp)
        if len(self.stack) == 1:
            return self.pop()
        return -1


exp = 'ab*c+'
c = Conversion(exp)
print c.postfix_to_infix()