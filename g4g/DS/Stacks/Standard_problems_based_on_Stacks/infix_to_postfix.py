''' Infix to Postfix '''


class Conversion(object):
    
    def __init__(self, exp):
        self.exp = exp
        self.stack = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def push(self, operation):
        self.stack.append(operation)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None

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
        for i in self.exp:
            if self.isOperand(i):
                output += i
            elif i == '(':
                self.push(i)
            elif i == ')':
                while not self.isEmpty() and self.peek() != '(':
                    op = self.pop()
                    output += op
                if not self.isEmpty and self.peek() != '(':
                    return -1
                else:
                    self.pop()
            else:
                while not self.isEmpty() and self.notGreater(i):
                    output += self.pop()
                self.push(i)
        while not self.isEmpty():
            output += self.pop()
        return output


exp = "a+b*(c^d-e)^(f+g*h)-i"
c = Conversion(exp)
print c.infix_to_postfix()
