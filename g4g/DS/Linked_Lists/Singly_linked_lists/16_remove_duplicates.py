'''
   Remove duplicates from a sorted linked list
'''

class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList(object):

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

    def remove_duplicates(self):
        cur = self.head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next

    def print_linked_list(self):
        cur = self.head
        while cur:
            print cur.val,
            cur = cur.next
        print '\n'


ll = LinkedList()
ll.push(1)
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(3)
ll.push(4)
ll.push(5)
ll.push(5)
ll.push(6)
ll.print_linked_list()
ll.remove_duplicates()
ll.print_linked_list()
