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

    def print_linked_list(self):
        cur = self.head
        while cur:
            print cur.val,
            cur = cur.next
    
    def reverse_portion(self, ref):
        prev = None
        cur = ref.next
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        ref.next = prev

    def reverse_complete(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev
    
    def get_middle(self):
        prev = None
        slow = self.head
        fast = self.head
        counter = 0
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            counter += 1
        return prev, counter
    
    def check_palindrome(self):
        prev, c = self.get_middle()
        self.reverse_portion(prev)
        first = self.head
        second = prev.next
        palin = True
        for _ in range(c):
            if first.val != second.val:
                palin = False
                break
            first = first.next
            second = second.next
        # Revert back to original Linked List
        self.reverse_portion(prev)
        return palin


ll = LinkedList()

ll.push('R')
ll.push('A')
ll.push('D')
ll.push('E')
ll.push('D')
ll.push('A')
ll.push('R')
print ll.check_palindrome()
ll.print_linked_list()
