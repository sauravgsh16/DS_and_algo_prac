''' Get nth element of a linked list '''

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

    def getNthIterative(self, n):
        counter = 0
        cur = self.head
        while counter != n and cur:
            cur = cur.next
            counter += 1
        
        if not cur:
            return None
        return cur.val
    
    def _getNthRecursive(self, node, n):
        count = 1
        if node:
            if count == n:
                return node.val
            else:
                self._getNthRecursive(node.next, n-1)
        else:
            return None
    
    def getNthRecursive(self, n):
        return self._getNthRecursive(self.head, n)

ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)

print ll.getNthIterative(0)
print ll.getNthRecursive(1)