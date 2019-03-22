'''
   Reverse a Linked List in groups of given size

   Inputs:  1->2->3->4->5->6->7->8->NULL and k = 3 
   Output:  3->2->1->6->5->4->8->7->NULL.
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

    def reverse_util(self, head, k):
        cur = head
        prev = None
        next = None
        count = 0

        while cur and count < k:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            count += 1
        
        if next:
            head.next = self.reverse_util(next, k)
        return prev
    
    def reverse(self, k):
        self.head = self.reverse_util(self.head, k)
    
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
ll.push(6) 
ll.push(7) 
ll.push(8) 
ll.push(9) 

ll.print_linked_list() 
print '\n'
ll.reverse(3) 

ll.print_linked_list()
print '\n'