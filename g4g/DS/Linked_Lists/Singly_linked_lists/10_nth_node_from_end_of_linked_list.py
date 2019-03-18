''' Get nth node from end of linked list '''

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

    def nth_node_from_end_first_method(self, n):
        # Traverve the complete linked list to find lenght
        # Then return length - n + 1 node.
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        
        if n > count:
            return -1
        cur = self.head
        for _ in range(count - n):
            cur = cur.next
        return cur.val

    def nth_node_from_end_second_method(self, n):
        # Maintain 2 pointer
        # Move first pointer to n places from head
        # Then move both pointers till first pointer reaches end
        # Return the second pointer.
        first = self.head
        second = self.head
        for _ in range(n):
            first = first.next
        
        while first:
            first = first.next
            second = second.next

        return second.val


ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)

print ll.nth_node_from_end_first_method(2)
print ll.nth_node_from_end_second_method(2)