''' Implementing Deque with doubly linked list '''

class Node(object):

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Deque(object):

    def __init__(self):
        self.front = None
        self.rear = None

    def insert_front(self, val):
        newNode = Node(val)
        if not self.front:
            self.front = newNode
            self.rear = newNode
        else:
            newNode.next = self.front
            self.front.prev = newNode
            self.front = newNode

    def insert_rear(self, val):
        newNode = Node(val)
        if not self.rear:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            newNode.prev = self.rear
            self.rear = newNode

    def delete_front(self):
        if not self.front:
            return -1
        node = self.front
        self.front = node.next
        if self.front == None:
            self.rear = None
        else:
            self.front.prev = None
        node.next = None
        return node.val

    def delete_rear(self):
        if not self.rear:
            return -1
        node = self.rear
        self.rear = node.prev
        if not self.rear:
            self.front = None
        else:
            self.rear.next = None
        node.prev = None
        return node.val

    def print_deque(self):
        cur = self.front
        while cur:
            print cur.val,
            cur = cur.next
        print '\n'


dq = Deque()
dq.insert_front(1)
dq.insert_front(2)
dq.insert_rear(3)
dq.insert_rear(4)
dq.print_deque()
print dq.delete_front()
dq.print_deque()
print dq.delete_rear()
dq.print_deque()