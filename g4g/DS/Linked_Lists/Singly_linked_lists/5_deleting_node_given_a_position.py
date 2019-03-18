''' Delete a Linked List node at a given position '''

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

    def deletePos(self, pos):
        if pos == 0:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp.val

        prev = self.head
        current = self.head.next
        counter = 1
        while counter != pos and current:
            prev = current
            current = current.next
            counter += 1
        
        if not current:
            return None
        
        prev.next = current.next
        return current.val

    def printList(self):
        temp = self.head
        while temp:
            print temp.val
            temp = temp.next

llist = LinkedList() 
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

llist.printList()
print 'Deleting'
print 'Returning', llist.deletePos(2)
llist.printList()