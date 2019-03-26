''' Implementing a DOUBLE ENDED QUEUE '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class CircularDeque(object):
    def __init__(self):
        self.front = None
        self.rear = None

    def insert_front(self, val):
        newNode = Node(val)
        if not self.front:
            self.front = self.rear = newNode
        else:
            newNode.next = self.front
            self.front = newNode
        self.rear.next = self.front

    def insert_rear(self, val):
        newNode = Node(val)
        if not self.rear:
            self.rear = self.front = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        self.rear.next = self.front

    def remove_front(self):
        if not self.front:
            return None
        node = self.front
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear.next = self.front.next
            self.front = self.rear.next
        return node.val

    def remove_rear(self):
        if not self.rear:
            return None
        node = self.rear
        if self.rear == self.front:
            self.rear = self.front = None
        else:
            prev = None
            cur = self.front
            while cur != self.rear:
                prev = cur
                cur = cur.next
            node = self.rear
            prev.next = self.rear.next
            self.rear = prev
        return node.val
            

    def print_deque(self):
        cur = self.front
        if cur:
            while True:
                print cur.val,
                cur = cur.next
                if cur == self.front:
                    break


cDQ = CircularDeque()
cDQ.insert_front(1)
cDQ.insert_front(2)
cDQ.insert_front(3)
cDQ.insert_rear(4)
cDQ.insert_rear(5)
cDQ.insert_rear(6)

cDQ.print_deque()
print '\n'
#print cDQ.front.val, cDQ.rear.val
for _ in range(3):
    print cDQ.front.val, cDQ.rear.val
    print cDQ.remove_front()
    print cDQ.remove_rear()
