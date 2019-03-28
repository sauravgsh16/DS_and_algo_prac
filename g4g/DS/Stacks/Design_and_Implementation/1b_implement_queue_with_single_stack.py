''' Implementing a Queue with a single stack '''

class Queue(object):

    def __init__(self):
        self.stack = []

    def enqueue(self, val):
        self.stack.append(val)

    def dequeue(self):
        if len(self.stack) == 0:
            return None
        
        val = self.stack.pop()
        if len(self.stack) == 0:
            return val
        
        item = self.dequeue()
        self.stack.append(val)
        return item


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)


print q.dequeue()