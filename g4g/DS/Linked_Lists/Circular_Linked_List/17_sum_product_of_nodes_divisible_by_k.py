''' Sum and Product of the nodes of a Circular Singly Linked List which are divisible by K '''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class CircularLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            newNode.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
            newNode.next = self.head
        self.size += 1


def sum_and_product(cll, k):
    sum = 0
    product = 1

    cur = cll.head
    while True:
        if cur.val % k == 0:
            sum += cur.val
            product *= cur.val
        cur = cur.next
        if cur == cll.head:
            break
    return sum, product


cll = CircularLinkedList()
cll.push(5)
cll.push(6)
cll.push(7)
cll.push(8)
cll.push(9)
cll.push(10)
cll.push(11)
cll.push(11)

print sum_and_product(cll, 11)