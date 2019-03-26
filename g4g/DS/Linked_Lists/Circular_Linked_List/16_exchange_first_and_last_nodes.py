''' Exchange first and last nodes of a Circular Linked List '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class CircularLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            newNode.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
            newNode.next = self.head
        self.size += 1

    def print_linked_list(self):
        cur = self.head
        if cur:
            while True:
                print cur.val,
                cur = cur.next
                if cur == self.head:
                    break
        print '\n'

    def exchange_first_last(self):
        if not self.head or self.size == 1:
            return
        prev = None
        cur = self.head
        while cur.next != self.head:
            prev = cur
            cur = cur.next
        prev.next = self.head
        cur.next = self.head.next
        self.head = cur
        prev.next.next = self.head


cll = CircularLinkedList()
cll.push(1)
cll.push(2)
cll.push(3)
cll.push(4)
cll.push(5)
cll.print_linked_list()
cll.exchange_first_last()
cll.print_linked_list()

