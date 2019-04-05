''' Implement a Stack and a Queue using a deque '''

'''
   Operations
   -----------------------------------------------
   Deque              Stack           Queue
   -----------------------------------------------
   insert_front        
   insert_rear         push           enQueue
   delete_front                       deQueue          
   delete_rear         pop
'''

''' We use a Doubly Linked List to implement a deque '''

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return 'Val -> {}'.format(self.val)


class Deque(object):

    def __init__(self):
        self.front = None
        self.rear = None

    def insert_rear(self, val):
        newNode = Node(val)
        if not self.rear:
            self.front = newNode
        else:
            self.rear.next = newNode
            newNode.prev = self.rear
        self.rear = newNode

    def delete_rear(self):
        node = self.rear
        if not node:
            return
        if node == self.front:
            self.front = self.rear = None
        else:
            self.rear.prev.next = None
            self.rear = self.rear.prev
        node.prev = None
        return node

    def delete_front(self):
        node = self.front
        if not node:
            return
        if node == self.rear:
            self.front = self.rear = None
        else:
            self.front.next.prev = None
            self.front = self.front.next
        node.next = None
        return node

    def print_deque(self):
        if not self.front:
            return
        cur = self.front
        while cur:
            print cur.val,
            cur = cur.next
        print '\n'

class Stack(object):
    
    def __init__(self):
        self.dq = Deque()

    def push(self, val):
        self.dq.insert_rear(val)
    
    def pop(self):
        return self.dq.delete_rear()


class Queue(object):

    def __init__(self):
        self.dq = Deque()

    def enQueue(self, val):
        self.dq.insert_rear(val)

    def deQueue(self):
        return self.dq.delete_front()

    def print_Queue(self):
        self.dq.print_deque()


print 'Stack Implementation'
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print s.pop()
print s.pop()
print s.pop()

print 'Queue Implementation'
q = Queue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)

print q.deQueue()
print q.deQueue()
print q.deQueue()
