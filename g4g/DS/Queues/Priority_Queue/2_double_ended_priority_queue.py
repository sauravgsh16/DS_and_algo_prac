''' Implement a double ended Priority Queue '''

'''
   Operations that need to be supported
   1) getMin
   2) getMax
   3) deleteMin
   4) deleteMax
   5) size
   6) isEmpty

   Data Structures which can be used are:
   1) Linked List:
      If we maintain the elements in a sorted order all above operations
      can be achived in O(1) time.
      Though insertion will be O(n)
    
   2) Use 2 heaps:
      Max heap and Min heap
      We maintain a pointer of every max heap element in the min heap.
      To get min - we return root of min heap
      To get max - we return root of max heap
      To insert elements , we insert in min heap and max heap.
      Idea is to maintain one-to-one correspondence, so that deleteMin() &
      deleteMax() can be done in O(log n) time.
      Disadvantage - Need extra O(n) for additional heap

   3) Use self balancing binary search tree.
      Supports all operations with same time complexity as second approach.
      Need to learn self balancing binary search tree before implementing
'''

# Implementing Linked List and Heap solution

''' Linked List '''

class Node_LL(object):
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
        self.next = None


class DoubleEndedPriorityQueue_linkedlist(object):

    def __init__(self):
        self.last = None

    def push(self, val, priority):
        newNode = Node_LL(val, priority)
        if not self.last:
            self.last = newNode
            self.last.next = newNode
        else:
            cur = self.last.next
            while True:
                while (cur.next != self.last.next
                    and newNode.priority > cur.next.priority):
                    cur = cur.next
                if cur.next == self.last.next:
                    newNode.next = self.last.next
                    self.last = newNode
                else:
                    newNode.next = cur.next
                cur.next = newNode
                break
    
    def getMin(self):
        return self.last.next.val

    def getMax(self):
        return self.last.val

    def deleteMin(self):
        if not self.last:
            return -1
        if self.last == self.last.next:
            node = self.last
            self.last = None
        else:
            node = self.last.next
            self.last.next = node.next
        return node.val

    def deteleMax(self):
        if not self.last:
            return -1
        cur = self.last.next
        while cur.next != self.last:
            cur = cur.next
        node = self.last
        cur.next = self.last.next
        self.last = cur
        node.next = None
        return node.val

    def print_list(self):
        cur = self.last.next
        if cur:
            while True:
                print cur.val,
                cur = cur.next
                if cur == self.last.next:
                    break
        print '\n'

pq = DoubleEndedPriorityQueue_linkedlist()
pq.push(10, 1)
pq.push(20, 2)
pq.push(40, 4)
pq.push(30, 3)

pq.print_list()

print 'Min', pq.getMin()
print 'Max', pq.getMax()
print 'deleted min', pq.deleteMin()
pq.print_list()
print 'deleted max', pq.deteleMax()
pq.print_list()

###################################################################

''' Double ended priority Queue using 2 heaps '''

class HeapNode(object):
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority


class DoubleEndedPriorityQueue_Heap(object):

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.size = 0

    def push(self, val, priority):
        newNode = HeapNode(val, priority)
        self.size += 1
        self.push_min(newNode)
        self.push_max(newNode)

    # INCOMPLETE
        