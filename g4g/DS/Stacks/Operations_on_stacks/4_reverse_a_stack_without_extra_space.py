''' Reverse a linked list without extra space '''

# Represent stack as a linked list

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack(object):
    def __init__(self):
        self.head = None

    def push(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        node = self.head
        self.head = node.next
        node.next = None
        return node.val

    def reverse_stack(self):
        cur = self.head
        prev = None
        while cur:
            next_next = cur.next
            cur.next = prev
            prev = cur
            cur = next_next
        self.head = prev

    def print_stack(self):
        cur = self.head
        while cur:
            print cur.val,
            cur = cur.next
        print '\n'


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)


s.print_stack()
s.reverse_stack()
print 'Printing reverse'
s.print_stack()