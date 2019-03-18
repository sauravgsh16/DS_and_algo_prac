''' No of times an int occurs in a linked list '''

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

    def get_frequency(self, key):
        cur = self.head
        count = 0
        while cur:
            if cur.val == key:
                count += 1
            cur = cur.next
        return count
    
    def get_frequency_recursive(self, key):
        self.count = 0
        def counter(node, key):
            if not node:
                return
            if node.val == key:
                self.count +=  1
            return counter(node.next, key)
        counter(self.head, key)
        return self.count


ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(1)
ll.push(4)
ll.push(1)

print ll.get_frequency(1)
print ll.get_frequency_recursive(1)