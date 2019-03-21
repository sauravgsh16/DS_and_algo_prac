''' Print reverse function of a linked list. Not actual reverse '''

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
    
    def print_reverse_util(self, head):
        if not head:
            return
        self.print_reverse_util(head.next)
        print head.val
    
    def print_reverse(self):
        if not self.head:
            return None
        self.print_reverse_util(self.head)


ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)

ll.print_reverse()