'''
   Pair wise swap
   1->2->3->4->5->6 
   2->1->4->3->6->5

   or 
   1->2->3->4->5
   2->1->4->3->5
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
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
        self.size += 1
        return self

    def print_linked_list(self):
        cur = self.head
        while cur:
            print cur.val,
            cur = cur.next
    
    def pair_wise_swap(self, head):
        if not head or not head.next:
            return head
        next_next = head.next.next
        result = head.next
        head.next.next = head
        head.next = self.pair_wise_swap(next_next)
        return result
    
    def swap(self):
        self.head = self.pair_wise_swap(self.head)

ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)

ll.print_linked_list()
print '\n'
ll.swap()
ll.print_linked_list()