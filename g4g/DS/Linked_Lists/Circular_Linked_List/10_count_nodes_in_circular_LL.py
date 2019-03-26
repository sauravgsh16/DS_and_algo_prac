''' Count number of nodes in CircularLinkedList '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class CircularLinkedList(object):
    def __init__(self):
        self.head = None

    def push(self, val):
        nN = Node(val)
        if not self.head:
            self.head = nN
            nN.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = nN
            nN.next = self.head

    def count_nodes(self):
        if not self.head:
            return 0
        cur = self.head
        count = 1
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count


arr = [1, 2, 3, 4, 5]
cll = CircularLinkedList()
for i in arr:
    cll.push(i)

print cll.count_nodes()