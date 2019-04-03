''' Convert expression from postfix to prefix '''
'''
   All steps are same as prefix, only differences are:
   1) NEED TO READ FROM LEFT TO RIGHT
   *******************************************
            IMPORTANT: CHECK ORDER
   2) EXPRESSION =  OPERATION + OP2 + OP1
   *******************************************
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

    def postfix_to_prefix(self):
        for i in self.exp:
            if self.isOperand(i):
                self.push(i)
            else:
                count = 0
                string = ''
                while not self.isEmpty() and count < 2:
                    string = self.pop() + string
                    count += 1
                exp = i + string
                self.push(exp)
        if len(self.stack) == 1:
            return self.pop()
        return -1

exp = 'ABC/-AK/L-*'
c = Conversion(exp)
print c.postfix_to_prefix()