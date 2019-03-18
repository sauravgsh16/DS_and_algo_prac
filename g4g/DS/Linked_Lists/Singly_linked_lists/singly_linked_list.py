'''
   Singly linked list
'''

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self
    
    def pop(self):
        if not self.head:
            return None
        current = self.head
        newTail = current
        while current.next:
            newTail = current
            current = current.next
        
        self.tail = newTail
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        
        return current

    def unshift(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        return self

    def insert(self, idx, val):
        if idx < 0 or idx > self.length:
            return None
        if idx == 0:
            return self.unshift(val)
        if idx == self.length:
            return self.push(val)
        counter = 1
        prev = self.head
        current = self.head.next
        while counter != idx:
            prev = current
            current = current.next
            counter += 1
        newNode = Node(val)
        prev.next = newNode
        newNode.next = current
        self.length += 1
