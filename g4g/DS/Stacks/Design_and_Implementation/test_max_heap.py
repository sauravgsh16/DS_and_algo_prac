class Node(object):
    def __init__(self, val, prio):
        self.val = val
        self.prio = prio

class MaxHeap(object):

    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, node):
        parent = (node - 1) // 2
        if parent == -1:
            return 0
        return parent

    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def push(self, val):
        newNode = Node(val, self.size)
        self.heap.append(newNode)
        self.size += 1
        if self.size == 1:
            return
        cur = self.size - 1
        while self.heap[cur].prio > self.heap[self.parent(cur)].prio:
            self.swap(cur, self.parent(cur))
            cur = self.parent(cur)

    def is_leaf(self, node):
        if node >= (self.size - 1) / 2 and node <= self.size - 1:
            return True
        return False

    def leftChild(self, node):
        return 2 * node + 1

    def rightChild(self, node):
        return 2 * node + 2

    def heapify(self, pos):
        if self.is_leaf(pos):
            return
        left = self.leftChild(pos)
        right = self.rightChild(pos)
        if self.heap[pos].prio < self.heap[left].prio or self.heap[pos].prio < self.heap[right].prio:
            if self.heap[left].prio > self.heap[right].prio:
                self.swap(pos, left)
                self.heapify(left)
            else:
                self.swap(pos, right)
                self.heapify(right)

    def pop(self):
        self.swap(0, self.size-1)
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
