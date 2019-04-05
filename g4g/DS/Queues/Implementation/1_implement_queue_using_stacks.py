''' Implement Queue using stacks '''

# METHOD 1:
# Making the dequeue operation expensive

class Queue1(object):

    def __init__(self):
        self.stack = []
        self.temp = []

    def enQueue(self, val):
        self.stack.append(val)

    def deQueue(self):
        if len(self.stack) == 0 and len(self.temp) == 0:
            return None
        if len(self.temp) == 0:
            while len(self.stack) != 0:
                self.temp.append(self.stack.pop())
        return self.temp.pop()


# METHOD 2:
# Making the enQueue operation expensive

class Queue2(object):
    def __init__(self):
        self.stack = []
        self.temp = []

    def enQueue(self, val):
        # Move all elements from stack to temp
        while len(self.stack) != 0:
            self.temp.append(self.stack.pop())
        self.stack.append(val)
        # Move all element from temp to stack
        while len(self.temp) != 0:
            self.stack.append(self.temp.pop())

    def deQueue(self):
        return self.stack.pop()

q1 = Queue1()
q2 = Queue2()

q1.enQueue(1)
q1.enQueue(2)
q1.enQueue(3)
q1.enQueue(4)
q1.enQueue(5)
print q1.deQueue()
print q1.deQueue()
print q1.deQueue()
print q1.deQueue()
print q1.deQueue()

q2.enQueue(6)
q2.enQueue(7)
q2.enQueue(8)
q2.enQueue(9)
q2.enQueue(10)

print q2.deQueue()
print q2.deQueue()
print q2.deQueue()
print q2.deQueue()
print q2.deQueue()