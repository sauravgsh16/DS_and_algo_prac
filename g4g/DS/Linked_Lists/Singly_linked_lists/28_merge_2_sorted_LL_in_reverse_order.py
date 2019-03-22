'''
   Merge two sorted linked lists such that merged list is in reverse order
'''

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

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def print_linked_list(self):
        cur = self.head
        while cur:
            print cur.val,
            cur = cur.next


def merge_reverse(l1, l2):
    cur1 = l1.head
    cur2 = l2.head

    result = LinkedList()
    next = None
    while cur1 and cur2:
        if cur1.val < cur2.val:
            if next is None:
                result.head = cur1
            else:
                next.next = cur1
            next = cur1
            cur1 = cur1.next
        else:
            if next is None:
                result.head = cur2
            else:
                next.next = cur2
            next = cur2
            cur2 = cur2.next

    while cur1:
        next.next= cur1
        cur1 = cur1.next
    
    while cur2:
        next.next = cur2
        cur2 = cur2.next
    
    result.reverse()
    return result
    
l1 = LinkedList()
l1.push(1)
l1.push(3)
l1.push(5)
l1.push(7)

l2 = LinkedList()
l2.push(2)
l2.push(4)
l2.push(6)

result = merge_reverse(l1, l2)
result.print_linked_list()
