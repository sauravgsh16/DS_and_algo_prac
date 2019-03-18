''' Get middle node of linked list '''

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

    def get_middle_method1(self):
        # Count the lenght of LL.
        # Return count/2 node
        count = 0
        cur = self.head
        while cur:
            cur = cur.next
            count += 1
        middle = count // 2
        cur = self.head
        for _ in range(middle):
            cur = cur.next
        return cur.val
    
    def get_middle_method_2(self):
        # Maintain two pointers
        # Move first pointer by one position and
        # the second by 2 positions.
        # when second reaches end, first will be in the middle
        fast = self.head
        slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.val

ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.push(6)

print ll.get_middle_method1()
print ll.get_middle_method_2()