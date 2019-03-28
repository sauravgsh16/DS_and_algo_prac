''' Reverse a doubly linked list '''

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


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

    def reverse(self):
        temp = None
        cur = self.head
        while cur:
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev
        
        if temp:
            self.head = temp.prev

    def print_list(self):
        last = None
        cur = self.head
        while cur:
            print cur.val,
            last = cur
            cur = cur.next
        print '\n'

        while last:
            print last.val,
            last = last.prev
        print '\n'

dll = DoublyLinkedList()
dll.push(1)
dll.push(2)
dll.push(3)
dll.push(4)
dll.print_list()
dll.reverse()
dll.print_list()
