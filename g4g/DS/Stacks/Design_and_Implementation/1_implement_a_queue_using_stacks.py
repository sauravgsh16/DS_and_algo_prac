''' Implementing a Queue using stacks '''

# METHOD 1
# Making the enqueue operation expensive

class Queue1(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, data):
        # Move all elements of stack1 to stack2
        while len(self.s1) != 0:
            val = self.s1.pop()
            self.s2.append(val)
        self.s1.append(data)
        # Push everything back to s1
        while len(self.s2) != 0:
            val = self.s2.pop()
            self.s1.append(val)
    
    def dequeue(self):
        if len(self.s1) == 0:
            return None
        val = self.s1.pop()
        return val



# Method 2
# Making the dequeue operation expensive

class Queue2(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, val):
        self.s1.append(val)

    def dequeue(self):
        if len(self.s1) == 0 and len(self.s2) == 0:
            return None
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                val = self.s1.pop()
                self.s2.append(val)
        data = self.s2.pop()
        return data


q1 = Queue1()
q1.enqueue(0)
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
print q1.dequeue()
print q1.dequeue()

print 'Queue 2 ops'
q2 = Queue2()
q2.enqueue(0)
q2.enqueue(1)
print q2.dequeue()
print q2.dequeue()
q2.enqueue(2)
q2.enqueue(3)
print q2.dequeue()