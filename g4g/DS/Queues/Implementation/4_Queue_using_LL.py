''' Implement Queue using Linked List '''

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return 'val -> {}'.format(self.val)


class Queue(object):

    def __init__(self):
        self.head = self.rear = None

    def isEmpty(self):
        return self.head == None

    def enQueue(self, val):
        newNode = Node(val)

        if self.rear == None:
            self.head = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def deQueue(self):
        if self.isEmpty():
            return
        node = self.head
        if node.next == None:
            self.rear = None
        else:
            self.head = node.next
            node.next = None
        return node


q = Queue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)

print q.deQueue()
print q.deQueue()