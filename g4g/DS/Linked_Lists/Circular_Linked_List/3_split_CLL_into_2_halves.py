'''
   Split a circular LL into 2 halves 
   If there are odd number of nodes, then first list should contain one extra
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class CircularLL(object):

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

    def print_linked_list(self):
        cur = self.head
        if cur:
            while True:
                print cur.val,
                cur = cur.next
                if cur == self.head:
                    break

    def split_list(self, cll1, cll2):
        slow = self.head
        fast = self.head
        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next
        
        # If list is even, we need to move fast pointer:
        if fast.next.next == self.head:
            fast = fast.next

        # Set head of first list
        cll1.head = self.head

        # Set head of second list
        if self.head.next != self.head:
            cll2.head = slow.next
        
        # Make second half circular
        fast.next = slow.next

        # Make first half circular
        slow.next = self.head


cll = CircularLL()
cll.push(1)
cll.push(2)
cll.push(3)
cll.push(4)
cll.push(5)
cll.push(6)

cll1 = CircularLL()
cll2 = CircularLL()
cll.split_list(cll1, cll2)

cll1.print_linked_list()
print '\n'
cll2.print_linked_list()