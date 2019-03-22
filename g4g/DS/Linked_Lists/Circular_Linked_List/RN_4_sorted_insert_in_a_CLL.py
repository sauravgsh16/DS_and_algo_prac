''' Sorted insert in a Circular Linked List '''

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class CircularLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    
    def _sorted_insert(self, val):
        newNode = Node(val)
        cur = self.head
        if not cur:
            self.head = newNode
            newNode.next = self.head
        elif cur.val >= newNode.val:
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
            newNode.next = self.head
            self.head = newNode
        else:
            while cur.next != self.head and cur.next.val < newNode.val:
                cur = cur.next
            newNode.next = cur.next
            cur.next = newNode
    
    def push(self, val):
        self._sorted_insert(val)
        self.size += 1

    def print_linked_list(self):
        cur = self.head
        if cur:
            while True:
                print cur.val,
                cur = cur.next
                if cur == self.head:
                    break

cll = CircularLinkedList()
cll.push(1)
cll.push(10)
cll.push(5)
cll.push(11)

cll.print_linked_list()