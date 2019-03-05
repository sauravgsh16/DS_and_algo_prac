'''
   Min heap implementation
'''

class MinHeap(object):

    def __init__(self):
        self.heap = []
        self.size = 0

    def _parent(self, node):
        parent = (node - 1) // 2
        if parent == -1:
            return 0
        return parent
    
    def _swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def insert(self, val):
        self.heap.append(val)
        self.size += 1
        if self.size == 1:
            return
        current = self.size - 1
        while self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _is_leaf(self, node):
        if node >= (self.size - 1 ) / 2 and node <= self.size - 1:
            return True
        return False

    def _left(self, pos):
        return 2 * pos + 1

    def _right(self, pos):
        return 2 * pos + 2

    def heapify(self, pos):
        if self._is_leaf(pos):
            return
        left = self._left(pos)
        right = self._right(pos)
        if self.heap[pos] > self.heap[left] or self.heap[pos] > self.heap[right]:
            if self.heap[left] < self.heap[right] or not self.heap[right]:
                self._swap(pos, left)
                self.heapify(left)
            else:
                self._swap(pos, right)
                self.heapify(right)

    def extractMin(self):
        self._swap(0, self.size-1)
        min = self.heap.pop()
        self.size -= 1
        self.heapify(0)
        return min

if __name__ == '__main__':
    heap = MinHeap()
    arr = [100, 70, 30, 40, 20, 10]
    for elem in arr:
        heap.insert(elem)
    print heap.extractMin()