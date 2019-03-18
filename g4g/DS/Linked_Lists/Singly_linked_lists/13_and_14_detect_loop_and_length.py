''' Detect loop in Linked List '''

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
    
    def detect_loop_using_hash_table(self):
        nodes = {}
        cur = self.head
        counter = 0
        while cur:
            if cur not in nodes.keys():
                nodes[cur] = counter
                counter += 1
                cur = cur.next
            else:
                return counter, nodes[cur]
        return False

    def detect_loop_efficient(self):
        # We use 2 pointers, fast and slow
        # If both pointers meet, then loop present
        fast = self.head
        slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def _detect_loop_efficient_returns_pointers(self):
        fast = self.head
        slow = self.head
        slow_counter = 0
        fast_counter = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            slow_counter += 1
            fast_counter += 2
            if slow == fast:
                return fast_counter, slow_counter

    def length_of_loop(self):
        f, s = self._detect_loop_efficient_returns_pointers()
        return f - s - 1

ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)

# Creating a loop
ll.tail.next = ll.head.next

#print ll.detect_loop_using_hash_table()
#print ll.detect_loop_efficient()
print ll.length_of_loop()