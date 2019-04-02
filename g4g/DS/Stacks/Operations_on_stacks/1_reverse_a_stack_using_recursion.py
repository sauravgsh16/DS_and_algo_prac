''' Reverse a stack '''

class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def print_stack(self):
        for i in range(len(self.stack)-1, -1, -1):
            print self.stack[i]

def reverse_stack(stack):
    if len(stack) == 0:
        return
    val = stack.pop(0)
    reverse_stack(stack)
    stack.append(val)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)


s.print_stack()
reverse_stack(s.stack)
print 'Printing reverse'
s.print_stack()