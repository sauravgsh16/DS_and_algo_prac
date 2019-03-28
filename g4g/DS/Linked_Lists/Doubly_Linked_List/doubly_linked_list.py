''' Implementation of a Doubly Linked List '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
            newNode.prev = cur
        self.size += 1
    
    def insert_beginning(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.size += 1

    def insert_after(self, item, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            cur = self.head
            while cur.val != item:
                cur = cur.next
            if not cur.next:
                return push(val)
            newNode.next = cur.next
            newNode.prev = cur
            cur.next.prev = newNode
            cur.next = newNode
        self.size += 1

    def print_list(self):
        cur = self.head
        if cur:
            while cur:
                print cur.val,
                cur = cur.next
        print '\n'

    def print_reverse(self):
        cur = self.head
        if cur:
            while cur.next:
                cur = cur.next
            while cur:
                print cur.val,
                cur = cur.prev
        print '\n'


dll = DoublyLinkedList()
dll.push(1)
dll.push(3)
dll.insert_beginning(4)
dll.insert_after(1, 2)
dll.insert_after(4, 5)
dll.print_list()
dll.print_reverse()