''' Implementation of a Queue '''

'''
   Pointers and methods which needs to be maintained/implemented are:
   1) front - pointer to front of queue
   2) rear - pointer to rear of queue
   3) capacity - capacity of the queue
   4) size - present size of the queue
   5) isFull - method to check queue is full
   6) isEmpty - method to check queue is empty
   7) enQueue - enqueue items in the rear
   8) deQueue - dequeue items from the front
   9) que_front - returns front of the queue
   10) que_rear - returns rear of the queue
'''

class Queue(object):

    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.capacity = capacity
        self.q = [None] * capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def enQueue(self, val):
        if self.isFull():
            return -1
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = val
        self.size += 1

    def deQueue(self):
        if self.isEmpty():
            return -1
        val = self.q[self.front]
        self.q[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return val

    def que_front(self):
        return self.q[self.front]

    def que_rear(self):
        return self.q[self.rear]


q = Queue(10)
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)

print q.deQueue()
print q.que_front()
print q.que_rear()

print q.q