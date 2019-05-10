''' Implementation of a binary Max Heap '''


class BinaryMaxHeap(object):
    def __init__(self):
        self.heap = []
        self.size = 0

    def _parent(self, idx):
        parent = (idx - 1) // 2
        if parent < 0:
            return 0
        return parent

    def _swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def insert(self, val):
        self.heap.append(val)
        self.size += 1
        if self.size == 1:
            return

        curr = self.size - 1
        while self.heap[curr] > self.heap[self._parent(curr)]:
            self._swap(curr, self._parent(curr))
            curr = self._parent(curr)

    def _is_leaf(self, pos):
        if pos >= (self.size - 1) // 2 and pos <= self.size - 1:
            return True
        return False

    def _get_left_child(self, pos):
        return 2 * pos + 1

    def _get_right_child(self, pos):
        return 2 * pos + 2

    def _heapify(self, pos):
        if self._is_leaf(pos):
            return

        left = self._get_left_child(pos)
        right = self._get_right_child(pos)

        if self.heap[pos] < self.heap[left] or self.heap[pos] < self.heap[right]:
            if self.heap[left] > self.heap[right]:
                self._swap(pos, left)
                self._heapify(left)
            else:
                self._swap(pos, right)
                self._heapify(right)

    def extract_max(self):
        self._swap(0, self.size - 1)
        val = self.heap.pop()
        self._heapify(0)
        return val


bh = BinaryMaxHeap()
bh.insert(100)
bh.insert(70)
bh.insert(30)
bh.insert(40)
bh.insert(20)
bh.insert(10)

print bh.heap
print bh.extract_max()
print bh.heap
