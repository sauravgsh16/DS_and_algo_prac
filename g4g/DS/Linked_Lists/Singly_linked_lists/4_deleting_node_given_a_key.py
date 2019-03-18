''' Delete a node, given a key '''

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
    
    def deleteKey(self, key):
        if self.head.val == key:
            self.head.next = self.head
            return
        
        prev = self.head
        current = self.head.next
        while current:
            if current.val == key:
                break
            prev = current
            current = current.next
        
        if not current:
            return None
        
        prev.next = current.next
        current.next = None
        return current
    
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
print 'Returning', llist.deleteKey(1).val
llist.printList()
