''' Median of Stream of Running Integers '''

class Heap(object):
    def __init__(self):
        self.heap = []
        self._size = 0

    def _parent(self, node):
        parent = (node - 1) // 2
        if parent < 0:
            return 0
        return parent

    def _swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def extract(self):
        self._swap(0, self._size - 1)
        val = self.heap.pop()
        self._size -= 1
        self._heapify(0)
        return val

    def _is_leaf(self, pos):
        if pos > ((self._size - 1) / 2) and pos <= self._size - 1:
            return True
        return False

    def _left_child(self, pos):
        left = 2 * pos + 1
        if left <= self._size - 1:
            return left
        return False

    def _right_child(self, pos):
        right = 2 * pos + 2
        if right <= self._size - 1:
            return right
        return False

    def print_heap(self):
        for val in self.heap:
            print val,
        print

    def size(self):
        return self._size

    def peek(self):
        return self.heap[0]

    def insert(self):
        raise NotImplementedError

    def _heapify(self):
        raise NotImplementedError

class MinHeap(Heap):

    def insert(self, val):
        self.heap.append(val)
        self._size += 1

        if self._size == 1:
            return
        curr = self._size - 1
        while self.heap[curr] < self.heap[self._parent(curr)]:
            self._swap(curr, self._parent(curr))
            curr = self._parent(curr)

    def _heapify(self, pos):
        if self._is_leaf(pos):
            return
        left = self._left_child(pos)
        right = self._right_child(pos)

        if left and right:
            if self.heap[pos] > self.heap[left] or self.heap[pos] > self.heap[right]:
                if self.heap[left] < self.heap[right] or not self.heap[right]:
                    self._swap(pos, left)
                    self._heapify(left)
                else:
                    self._swap(pos, right)
                    self._heapify(right)
        elif left:
            if self.heap[pos] > self.heap[left]:
                self._swap(pos, left)
                self._heapify(left)


class MaxHeap(Heap):

    def insert(self, val):
        self.heap.append(val)
        self._size += 1

        if self._size == 1:
            return
        curr = self._size - 1
        while self.heap[curr] > self.heap[self._parent(curr)]:
            self._swap(curr, self._parent(curr))
            curr = self._parent(curr)

    def _heapify(self, pos):
        if self._is_leaf(pos):
            return

        left = self._left_child(pos)
        right = self._right_child(pos)

        if right and left:
            if self.heap[pos] < self.heap[left] or self.heap[pos] < self.heap[right]:
                if self.heap[left] > self.heap[right]:
                    self._swap(pos, left)
                    self._heapify(left)
                else:
                    self._swap(pos, right)
                    self._heapify(right)
        elif left:
            if self.heap[pos] < self.heap[left]:
                self._swap(pos, left)
                self._heapify(left)


def get_median(arr):

    # ***** IMP ****
    # MIN HEAP WILL STORE THE GREATER ELEMENTS
    # MAX HEAP WILL STORE THE SMALLER ELEMENTS

    minHeap = MinHeap()
    maxHeap = MaxHeap()
    median_arr = []
    median = arr[0]
    median_arr.append(median)
    minHeap.insert(arr[0])

    for i in range(1, len(arr)):
        x = arr[i]
        # Case 1: Min side has more elements
        if minHeap.size() > maxHeap.size():
            '''
            NEED TO CHECK INCOMING IS GREATER THAN MINUMUM IN MIN HEAP
            '''
            if minHeap.peek() < x:
                val = minHeap.extract()
                maxHeap.insert(val)
                minHeap.insert(x)
            else:
                maxHeap.insert(x)
            median = (minHeap.peek() + maxHeap.peek()) / 2.0
        # Case 2: Both have equal elements
        elif minHeap.size() == maxHeap.size():
            if minHeap.peek() < x:
                val = minHeap.extract()
                maxHeap.insert(val)
                minHeap.insert(x)
            else:
                maxHeap.insert(x)
            median = maxHeap.peek()
        # Case 3: Max side has more elements
        else:
            '''
            NEED TO CHECK INCOMING IS SMALLER THAN MAXIMUM IN MAX HEAP
            '''
            if maxHeap.peek() > x:
                val = maxHeap.extract()
                minHeap.insert(val)
                maxHeap.insert(x)
            else:
                minHeap.insert(x)
            median = (minHeap.peek() + maxHeap.peek()) / 2.0

        median_arr.append(median)
    return map(float, median_arr)


arr1 = [5, 15, 10, 20, 3]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr3 = [11270, 86326, 58142, 71911, 91654, 9152, 16550, 71660, 73448, 67812, 4158, 48414]
print get_median(arr3)
