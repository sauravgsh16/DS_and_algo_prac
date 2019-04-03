''' Convert prefix to postfix '''

'''
   Read exp from right to left
   push operand to stack
   if operator is encountered, then pop 2 operands from stack.
   Concatenate the 2 operands with the operator in between and push it to stack
   Repeat process until end of expression
'''
# IMPORTANT NOTE:
# EXPRESSION = OP1 + OPERATION + OP2

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

    def prefix_to_infix(self):
        for i in range(len(self.exp)-1, -1, -1):
            ch = self.exp[i]
            if self.isOperand(ch):
                self.push(ch)
            else:
                count = 0
                string = []
                while not self.isEmpty() and count < 2:
                    string.append(self.pop())
                    count += 1
                exp = ch.join(string)
                exp = '(' + exp + ')'
                self.push(exp)
        if len(self.stack) == 1:
            return self.pop()
        return -1

exp = '*+AB-CD'
c = Conversion(exp)
print c.prefix_to_infix()