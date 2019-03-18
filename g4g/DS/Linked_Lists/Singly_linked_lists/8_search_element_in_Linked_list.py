''' Search an element in a Linked List (Iterative and Recursive) '''

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
        nN = Node(val)
        if not self.head:
            self.head = nN
            self.tail = nN
        else:
            self.tail.next = nN
            self.tail = nN
        self.size += 1
    
    def searchIterative(self, key):
        if self.head.val == key:
            return self.head.val
        
        cur = self.head.next
        while cur:
            if cur.val == key:
                return cur.val
            cur = cur.next
        return None
    
    def _searchRecursive(self, node, key):
        if node.val == key:
            return node.val
        if not node:
            return None
        return self._searchRecursive(node.next, key)

    def searchRecursive(self, key):
        return self._searchRecursive(self.head, key)


ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)

print ll.searchIterative(10)
print ll.searchRecursive(2)