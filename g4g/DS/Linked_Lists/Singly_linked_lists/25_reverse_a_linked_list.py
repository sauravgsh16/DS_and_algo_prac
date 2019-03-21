''' Reverse a linked list '''

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList(object):

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
        self.size += 1
    
    def reverse_iterative(self):
        if not self.head:
            return
        cur = self.head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def reverse_util(self, cur, prev):
        # If last node mark it head 
        if not cur.next:
            self.head = cur
            # Update next to prev node
            cur.next = prev
            return
        # Save cur.next node for recursive call
        next = cur.next
        # And update next
        cur.next = prev
        return self.reverse_util(next, cur)

    def reverse_recursive(self):
        if not self.head:
            return
        self.reverse_util(self.head, None)
    
    def print_linked_list(self):
        cur = self.head
        while cur:
            print cur.val,
            cur = cur.next


ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)

ll.print_linked_list()
print '\n'
ll.reverse_iterative()
ll.print_linked_list()
ll.reverse_recursive()
print '\n'
ll.print_linked_list()
