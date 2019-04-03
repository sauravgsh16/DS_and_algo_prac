''' Implementing a Priority Queue using a Linked List '''
'''
   Operations of a Priority Queue
   1) push
   2) pop
   3) peek / top
'''

class Node(object):

    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
        self.next = None


class PriorityQueue(object):

    def __init__(self):
        self.head = None

    def push(self, val, priority):
        newNode = Node(val, priority)
        if not self.head:
            self.head = newNode
        elif newNode.priority < self.head.priority:
            newNode.next = self.head
            self.head = newNode
        else:
            cur = self.head
            while cur.next and newNode.priority > cur.next.priority:
                cur = cur.next
            newNode.next = cur.next
            cur.next = newNode

    def pop(self):
        if not self.head:
            return -1
        node = self.head
        self.head = self.head.next
        return node.val

    def peek(self):
        if not self.head:
            return -1
        return self.head.val

    def print_queue(self):
        cur = self.head
        while cur:
            print cur.val,
            cur = cur.next
        print '\n'


pq = PriorityQueue()
pq.push(10, 1)
pq.push(20, 2)
pq.push(40, 4)
pq.push(30, 3)

pq.print_queue()

print pq.pop()
print pq.pop()

pq.print_queue()
print pq.peek()