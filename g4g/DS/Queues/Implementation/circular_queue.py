''' Implementing a circular Queue '''

class CircularQueue(object):
    def __init__(self, size):
        self.size = size
        self.q = [None] * size
        self.front = self.rear = -1

    def enQueue(self, val):
        if (self.rear + 1) % self.size == self.front:
            print 'Queue full'
            return
        if self.front == -1:
            self.front = 0
            self.rear = 0
            self.q[self.rear] = val
        else:
            self.rear = (self.rear + 1) % self.size
            self.q[self.rear] = val

    def deQueue(self):
        if self.front == -1:
            print 'Queue Empty'
            return
        if self.front == self.rear:
            val = self.q[self.front]
            self.front = self.rear = -1
        else:
            val = self.q[self.front]
            self.front = (self.front + 1) % self.size
        return val

    def print_queue(self):
        if self.front == -1:
            print 'Queue empty'
        elif self.rear >= self.front:
            for i in range(self.front, self.rear+1):
                print self.q[i],
        else:
            for i in range(self.front, self.size):
                print self.q[i]
            for i in range(0, self.rear+1):
                print self.q[i]
        if (self.rear + 1) % self.size == self.front:
            print 'Queue Full'