'''
   Segregate even and odd nodes
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
        return self
    
    def printList(self):
        temp = self.head
        while temp:
            print temp.val
            temp = temp.next
    
    def segregate_even_and_odd(self):
        cur = self.head
        end = self.head
        prev = None

        while end.next:
            end = end.next
        
        newEnd = end
        while (cur.val % 2 != 0) and cur != end:
            newEnd.next = cur
            cur = cur.next
            newEnd.next.next = None
            newEnd = newEnd.next

        if cur.val % 2 == 0:
            self.head = cur
            while cur != end:
                if cur.val % 2 == 0:
                    prev = cur
                    cur = cur.next
                else:
                    prev.next = cur.next
                    cur.next = None
                    newEnd.next = cur
                    newEnd = cur
                    cur = prev.next
        else:
            prev = cur
        
        if newEnd != end and (end.val % 2 != 0):
            prev.next = end.next
            end.next = None
            newEnd.next = end


ll = LinkedList()
#ll.push(17)
ll.push(18)
ll.push(19)
ll.push(20)
ll.push(21)

ll.segregate_even_and_odd()
ll.printList()