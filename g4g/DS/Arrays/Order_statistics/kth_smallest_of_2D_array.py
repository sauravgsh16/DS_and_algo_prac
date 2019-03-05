'''
   Kth smallest element in a row-wise and column-wise sorted 2D array

   10, 20, 30, 40
   15, 25, 35, 45
   24, 29, 37, 48
   32, 33, 39, 50
   The 3rd smallest element is 20 and 7th smallest element is 30
'''

class Node(object):
    def __init__(self, val, row, col):
        self.val = val
        self.row = row
        self.col = col


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

    def insert(self, val, row, col):
        nN = Node(val, row, col)
        self.heap.append(nN)
        self.size += 1
        if self.size == 1:
            return
        current = self.size - 1
        while self.heap[current].val < self.heap[self._parent(current)].val:
            self._swap(current, self._parent(current))
            current = self._parent(current)
    
    def _left(self, pos):
        return 2 * pos + 1

    def _right(self, pos):
        return 2 * pos + 2

    def _is_leaf(self, pos):
        if pos >= (self.size - 1) / 2 and pos <= self.size - 1:
            return True
        return False

    def heapify(self, pos):
        if self._is_leaf(pos):
            return
        left = self._left(pos)
        right = self._right(pos)
        current = self.heap[pos]
        if current.val > self.heap[left].val or current.val > self.heap[right].val:
            if self.heap[left].val < self.heap[right].val or not self.heap[right]:
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

def kthSmallestElem(heap, k):
    min = -1
    for i in range(k):
        min = heap.extractMin()
    return min.val

if __name__ == '__main__':
    heap = MinHeap()
    arr = [
        [10, 20, 30, 40], 
        [15, 25, 35, 45],
        [25, 29, 37, 48],
        [32, 33, 39, 50],
    ]
    for rowId, row in enumerate(arr):
        for colId, val in enumerate(row):
            heap.insert(val, rowId, colId)
    print kthSmallestElem(heap, 7)