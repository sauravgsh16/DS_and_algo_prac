''' Implementation of a circular linked list '''

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
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head
        self.size += 1

    def  print_linked_list(self):
        cur = self.head
        if cur:
            while True:
                print cur.val,
                cur = cur.next
                if cur == self.head:
                    break


cll = CircularLinkedList()
cll.push(1)
cll.push(2)
cll.push(3)
cll.push(4)

cll.print_linked_list()

        