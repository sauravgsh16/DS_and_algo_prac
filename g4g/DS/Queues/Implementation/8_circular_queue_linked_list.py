''' Circular Queue implementation using Linked List '''

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return 'Val -> {}'.format(self.val)


class CircularQueue(object):

    def __init__(self):
        self.rear = None

    def enQueue(self, val):
        newNode = Node(val)
        if not self.rear:
            self.rear = newNode
            newNode.next = self.rear
        else:
            newNode.next = self.rear.next
            self.rear.next = newNode
            self.rear = newNode
        cur = self.rear

    def deQueue(self):
        if not self.rear:
            return -1
        node = self.rear.next
        if node == self.rear:
            self.rear = None
        else:
            self.rear.next = node.next
        return node

    def print_queue(self):
        if not self.rear:
            return
        cur = self.rear.next
        while True:
            print cur.val,
            cur = cur.next
            if cur == self.rear.next:
                break
        print '\n'

cq = CircularQueue()
cq.enQueue(1)
cq.enQueue(2)
cq.enQueue(3)
cq.enQueue(4)
cq.enQueue(5)


cq.print_queue()

print cq.deQueue()
print cq.deQueue()

cq.print_queue()

