''' Implementing a Circular Queue '''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class CircularLinkedList(object):

    def __init__(self):
        self.front = None
        self.rear = None

    def enQueue(self, val):
        newNode = Node(val)
        if not self.front:
            self.front = newNode
        else:
            self.rear.next = newNode
        self.rear = newNode
        self.rear.next = self.front

    def deQueue(self):
        if not self.front:
            return None
        if self.front == self.rear:
            node = self.front
            self.front = self.rear = None
        else:
            node = self.front
            self.rear.next = self.front.next
            self.front = self.rear.next
        return node.val

    def print_linked_list(self):
        cur = self.front
        if cur:
            while True:
                print cur.val,
                cur = cur.next
                if cur == self.front:
                    break


cll = CircularLinkedList()
 

# Inserting elements in Circular Queue  
cll.enQueue(14)
cll.enQueue(22)
cll.enQueue(6)  

# Display elements present in  
# Circular Queue  
cll.print_linked_list()
print '\n'
# Deleting elements from Circular Queue  
print("Deleted value = ", cll.deQueue())
print("Deleted value = ", cll.deQueue())

# Remaining elements in Circular Queue  
cll.print_linked_list()
cll.enQueue(9)  
cll.enQueue(20)
print '\n'
cll.print_linked_list()
