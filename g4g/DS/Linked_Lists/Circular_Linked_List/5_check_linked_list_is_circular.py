''' Check if a Linked List is a circular link list '''

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
    
    def isCircular(self):
        cur = self.head
        while cur.next != self.head and cur.next:
            cur = cur.next
        return cur.next == self.head


cll = CircularLinkedList()
cll.push(1)
cll.push(2)
cll.push(3)
cll.push(4)

print cll.isCircular()