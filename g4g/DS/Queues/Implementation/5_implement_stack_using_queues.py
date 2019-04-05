''' Implement stack using Queues '''

from Queue import Queue


# Making pop operation expensive

class Stack1(object):

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, val):
        self.q1.put(val)

    def pop(self):
        if self.q1.empty():
            return -1
        while self.q1.qsize() != 1:
            popped = self.q1.get()
            self.q2.put(popped)
        val = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        return val


# Making the push operation expensive

class Stack2(object):

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, val):
        self.q2.put(val)
        while not self.q1.empty():
            popped = self.q1.get()
            self.q2.put(popped)
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.get()

s1 = Stack1()
s2 = Stack2()

for i in range(1, 6):
    s1.push(i)
    s2.push(i)

for _ in range(5):
    print s1.pop()
    print s2.pop()