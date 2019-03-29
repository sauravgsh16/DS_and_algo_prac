''' Implement stack using priority queue or heap '''

import sys

class Node(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority


class MaxHeap(object):

    def __init__(self):
        self.heap = []
        self.size = 0
        self.counter = sys.maxsize

    def parent(self, node):
        parent = (node - 1) // 2
        if parent == -1:
            return 0
        return parent

    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def push(self, val):
        newNode = Node(val, self.counter)
        self.heap.append(newNode)
        self.size += 1
        self.counter -= 1
        if self.size == 1:
            return

        cur = self.size - 1
        while self.heap[cur].priority < self.heap[self.parent(cur)].priority:
            self.swap(cur, self.parent(cur))
            cur = self.parent(cur)

    def pop(self):
        pass



m = MaxHeap()
m.push(1)
m.push(10)
m.push(5)
m.push(20)

for i in m.heap:
    print i.item