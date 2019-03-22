''' Insertion and deletion in a Circular Linked List '''

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class CircularLinkedList(object):
    def __init__(self):
        self.last = None
    
    def insert_beginning(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            newNode.next = self.head
        else:


# IMPLEMENTATION INCOMPLETE