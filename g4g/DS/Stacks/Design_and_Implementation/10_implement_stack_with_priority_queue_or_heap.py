''' Implement stack using priority queue or heap '''

import sys

class Node(object):
    def __init__(self, val, priority):
        self.val = val
        self.p = priority


class MaxHeap(object):

    def __init__(self):
        self.heap = []
        self.size = 0

    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def parent(self, node):
        parent = (node - 1) // 2
        if parent == -1:
            return 0
        return parent

    def push(self, val):
        newNode = Node(val, self.size)
        self.heap.append(newNode)
        self.size += 1
        if self.size == 1:
            return
        cur = self.size - 1
        while self.heap[cur].p > self.heap[self.parent(cur)].p:
            self.swap(cur, self.parent(cur))
            cur = self.parent(cur)

    def is_leaf(self, node):
        if node >= (self.size - 1) / 2 and node <= self.size - 1:
            return True
        return False

    def left_child(self, node):
        return 2 * node + 1

    def right_child(self, node):
        return 2 * node + 2

    def heapify(self, pos):
        if self.is_leaf(pos):
            return
        left = self.left_child(pos)
        right = self.right_child(pos)
        if self.heap[pos].p < self.heap[left].p or self.heap[pos].p < self.heap[right].p:
            if self.heap[left].p > self.heap[right].p:
                self.swap(pos, left)
                self.heapify(left)
            else:
                self.swap(pos, right)
                self.heapify(right)

    def pop(self):
        self.swap(0, self.size - 1)
        m = self.heap.pop()
        self.size -= 1
        self.heapify(0)
        return m.val

m = MaxHeap()
m.push(1)
m.push(10)
m.push(5)
m.push(20)
print 'Popped', m.pop()
print 'Popped', m.pop()
print 'Popped', m.pop()

for i in m.heap:
    print i.val