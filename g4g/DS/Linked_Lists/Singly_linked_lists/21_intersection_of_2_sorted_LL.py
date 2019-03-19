'''
   Intersection of two Sorted Linked Lists
   For example, let the first linked list be 1->2->3->4->6 and 
   second linked list be 2->4->6->8, 
   then function should create and return a third list as 2->4->6.
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
    
    def print_linked_list(self):
        cur = self.head
        while cur:
            print cur.val,
            cur = cur.next


def intersection_iterative(first, second):
    newList = LinkedList()
    f = first.head
    s = second.head
    while f and s:
        if f.val == s.val:
            newList.push(f.val)
            f = f.next
            s = s.next
        elif f.val < s.val:
            f = f.next
        else:
            s = s.next
    return newList

def intersection_recursive(first, second, newList):
    if not first or not second:
        return
    if first.val == second.val:
        newList.push(first.val)
        return intersection_recursive(first.next, second.next, newList)
    elif first.val < second.val:
        return intersection_recursive(first.next, second, newList)
    else:
        return intersection_recursive(first, second.next, newList)


l1 = LinkedList()
l1.push(1)
l1.push(2)
l1.push(3)
l1.push(4)
l1.push(6)

l2 = LinkedList()
l2.push(2)
l2.push(4)
l2.push(6)
l2.push(8)

nl = intersection_iterative(l1, l2)
nl.print_linked_list()
print '\n'
nlR = LinkedList()
intersection_recursive(l1.head, l2.head, nlR)
nlR.print_linked_list()