''' Implement a stack with a single Queue '''

from Queue import Queue


class Stack(object):

    def __init__(self):
        self.q = Queue()

    def push(self, val):
        size = self.q.qsize()
        self.q.put(val)

        while size != 0:
            val = self.q.get()
            self.q.put(val)
            size -= 1

    def pop(self):
        return self.q.get()


s = Stack()
s.push(1)
s.push(10)
s.push(100)

print s.pop()
print s.pop()
print s.pop()