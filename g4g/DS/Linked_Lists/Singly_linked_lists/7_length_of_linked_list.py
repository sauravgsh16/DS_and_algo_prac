''' Find length of LL, iterative and recursive '''

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

    def lengthIterative(self):
        if not self.head:
            return 0
        cur = self.head
        counter = 0
        while cur:
            counter += 1
            cur = cur.next
        return counter

    def _lenghtRecursive(self, node):
        if not node:
            return 0
        return 1 + self._lenghtRecursive(node.next)

    def lenghtRecursive(self):
        return self._lenghtRecursive(self.head)

ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)

print ll.lengthIterative()
print ll.lenghtRecursive()
