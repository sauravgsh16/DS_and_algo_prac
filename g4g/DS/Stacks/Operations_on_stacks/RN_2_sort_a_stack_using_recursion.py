''' Sort a stack using recursion '''

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        val = self.stack.pop()
        return val

    def top(self):
        return self.stack[-1]

    def sort(self):
        if len(self.stack) != 0:
            val = self.stack.pop()
            self.sort()
            self.sorted_insert(val)

    def sorted_insert(self, val):
        if len(self.stack) == 0 or val > self.top():
            self.push(val)
        else:
            top = self.stack.pop()
            self.sorted_insert(val)
            self.push(top)


s = Stack()
s.push(3)
s.push(2)
s.push(5)
s.push(4)
s.push(1)

s.sort()
print s.stack