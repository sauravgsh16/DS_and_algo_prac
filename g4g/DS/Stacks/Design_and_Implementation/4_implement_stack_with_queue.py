''' Implement a stack with Queues '''

from Queue import Queue


# METHOD 1: Making the pop operation costly
'''
push(x)
    Enqueue x to queue 1
pop()
    1) Dequeue all elements from queue1 to queue2 except last element.
    2) Dequeue last element and store it to return
    3) Swap queue 1 and queue 2. This is done to avoid more movements

'''

class Stack1(object):

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, val):
        self.q1.put(val)

    def pop(self):
        if self.q1.qsize() == 0:
            return None
        while self.q1.qsize() != 1:
            val = self.q1.get()
            self.q2.put(val)
        poppedVal = self.q1.get()
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp
        return poppedVal


s1 = Stack1()
for i in range(1, 6):
    s1.push(i)

for _ in range(5):
    print s1.pop(),


# METHOD 2: Making the push operation expensive
'''
push(x)
    1) Push x to q2
    2) While q1 is not empty, move all to q2
    3) Swap q1 and q2

pop()
    Pop from q1
'''
class Stack2(object):

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, val):
        self.q2.put(val)

        while not self.q1.empty():
            val = self.q1.get()
            self.q2.put(val)
        
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

    def pop(self):
        if self.q1.empty():
            return None
        return self.q1.get()

print '\nSecond method implemention'
s2 = Stack2()
for i in range(1, 6):
    s2.push(i)

for _ in range(5):
    print s2.pop(),
