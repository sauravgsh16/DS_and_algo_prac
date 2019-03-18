'''
   Function to check if a singly linked list is palindrome
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

    def check_palindrome(self):
        # Method 1:
        # Traverse the complete list, add each element in a stack
        # Traverse the list again, for each element- pop an element
        # from the stack and check if it is equal.
        # Space - O(n) - needs extra space to store stack
        cur = self.head
        stack = []
        while cur:
            stack.append(cur.val)
            cur = cur.next

        palin = True
        cur = self.head
        while cur and len(stack) > 0:
            ele = stack.pop()
            if ele != cur.val:
                palin = False
                break
            cur = cur.next
        return palin

    def reverse_linked_list(self, ref):
        prev = None
        cur = ref
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        ref = prev
    
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
    
    def check_palindrome_efficient(self):
        # Method 2:
        # Find the middle of the LinkedList
        # Reverse the second part of the LinkedList
        # Check if the reversed list is equal to first part of the LinkedList
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
print ll.check_palindrome_efficient()
ll.print_linked_list()