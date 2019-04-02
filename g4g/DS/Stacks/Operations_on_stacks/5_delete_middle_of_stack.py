''' Delete middle of stack '''

class Stack(object):

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, val):
        self.stack.append(val)
        self.size += 1

    def pop(self):
        val = self.stack.pop()
        if val:
            self.size -= 1
            return val
        return None

    def delete_middle(self, curr):
        if len(self.stack) == 0 or curr == self.size:
            return
        val = self.pop()
        self.delete_middle(curr + 1)
        if curr != (self.size / 2) + 1:
            self.push(val)    


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)

print s.size
s.delete_middle(0)
print s.stack
