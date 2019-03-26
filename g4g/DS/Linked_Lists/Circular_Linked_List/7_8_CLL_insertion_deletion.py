''' Insertion and deletion in a Circular Linked List '''

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class CircularLinkedList(object):
    def __init__(self):
        self.last = None

    def insert_empty(self, val):
        newNode = Node(val)
        if not self.last:
            self.last = newNode
            self.last.next = newNode
    
    def insert_beginning(self, val):
        if not self.last:
            return self.insert_empty(val)
        newNode = Node(val)
        newNode.next = self.last.next
        self.last.next = newNode

    def insert_end(self, val):
        if not self.last:
            return self.insert_empty(val)
        newNode = Node(val)
        newNode.next = self.last.next
        self.last.next = newNode
        self.last = newNode

    def insert_after(self, item, val):
        if not self.last:
            return self.insert_empty(val)
        cur = self.last.next
        newNode = Node(val)
        while True:
            if cur.val == item:
                newNode.next = cur.next
                cur.next = newNode
                if cur == self.last:
                    self.last = newNode
                return
            else:
                cur = cur.next
            if cur == self.last.next:
                break 

    def delete_beginning(self):
        node = self.last.next
        self.last.next = node.next
        node.next = None
        return node.val

    def delete(self, key):
        head = self.last.next
        cur = head
        prev = self.last
        while True:
            if cur.val == key:
                prev.next = cur.next
                if cur == self.last:
                    self.last = prev
                cur.next = None
                return cur.val
            prev = cur
            cur = cur.next
            if cur == head:
                break
        return None


    def print_linked_list(self):
        cur = self.last.next
        if cur:
            while True:
                print cur.val,
                cur = cur.next
                if cur == self.last.next:
                    break
        print '\n'


cll = CircularLinkedList()
cll.insert_empty(1)
cll.print_linked_list()
cll.insert_beginning(2)
cll.insert_beginning(3)
cll.insert_beginning(4)
cll.print_linked_list()
cll.insert_end(5)
cll.insert_end(6)
cll.insert_end(8)
cll.insert_end(9)
cll.print_linked_list()
cll.insert_after(6, 7)
cll.insert_after(9, 10)
cll.print_linked_list()

for _ in range(3):
    print cll.delete_beginning()
cll.print_linked_list()
print cll.delete(1)
cll.print_linked_list()
print cll.delete(7)
cll.print_linked_list()
print cll.delete(10)
cll.print_linked_list()
