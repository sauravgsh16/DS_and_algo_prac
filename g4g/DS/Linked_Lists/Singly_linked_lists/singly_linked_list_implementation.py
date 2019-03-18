''' Singly Linked List '''

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, val):
        newNode = Node(val)

        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return self
    
    def unshift(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        return self

    def insertAfter(self, val, index):
        if index < 0 or index > self.size:
            return -1
        if index == 0:
            return self.unshift(val)
        if index == self.size:
            return self.push(val)
        prev = self.head
        current = self.head.next
        counter = 1
        while counter != index:
            prev = current
            current = prev.next
            counter += 1
        newNode = Node(val)
        prev.next = newNode
        newNode.next = current
        self.size += 1
