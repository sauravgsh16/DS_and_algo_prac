''' Convert prefix to postfix '''
'''
   Same as prefix to infix, only difference is as below:
   # EXPRESSION = OP1 + OP2 + OPERATION
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

    def prefix_to_postfix(self):
        for i in range(len(self.exp)-1, -1, -1):
            ch = self.exp[i]
            if self.isOperand(ch):
                self.push(ch)
            else:
                count = 0
                string = ''
                while not self.isEmpty() and count < 2:
                    string += self.pop()
                    count += 1
                exp = string + ch
                self.push(exp)
        if len(self.stack) == 1:
            return self.pop()
        return -1


exp = '*-A/BC-/AKL'
c = Conversion(exp)
print c.prefix_to_postfix()