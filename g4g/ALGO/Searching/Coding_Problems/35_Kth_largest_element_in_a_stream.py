''' Find the Kth largest element in a stream '''

'''
   Input:
   stream = {10, 20, 11, 70, 50, 40, 100, 5, ...}
   k = 3

   Output:   _, _, 10, 11, 20, 40, 50, .....
'''

'''
   We can use a self balancing binary search tree of size k. The largest element
   can be found in O(logk) time.
   To process a new element:
   Check if new element is smaller than current kth largest element. If yes,
   then ignore it. If no, then remove the smallest element from the tree and insert
   new element. Time complexity of processing new element is O(logk)


   An efficient solution is to use a Min Heap of size k. To store k largest
   elements. The k'th largest is always the root and can be found in O(1) time.
   To process a new element:
   Compare new element with the root. If new element is smaller, then ignore it.
   Otherwise replace root with new element and call heapify for the root.
   Time complexity of finding the k'th largest element is O(logk)
'''

class MinHeap(object):
    def __init__(self, k):
        self.heap = []
        self.size = 0
        self.max_size = k

    def _parent(self, idx):
        return (idx - 1) // 2

    def _swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def insert(self, val):
        if self.size == self.max_size:
            self._replace(val)
        else:
            self.heap.append(val)
            self.size += 1

            if self.size != 1:
                current = self.size - 1
                while self.heap[current] > self.heap[self._parent(current)]:
                    self._swap(current, self._parent(current))
                    current = self._parent(current)
            if self.size == self.max_size:
                    print self._peek(),
            else:
                print "_",

    def _peek(self):
        return self.heap[0]

    def _is_leaf(self, pos):
        if pos >= (self.size - 1) / 2 and pos <= self.size - 1:
            return True
        return False

    def _left_child(self, pos):
        left = 2 * pos + 1
        if left <= self.size - 1:
            return left
        return -1

    def _right_child(self, pos):
        right = 2 * pos + 2
        if right <= self.size - 1:
            return right
        return -1

    def _heapify(self, pos):
        if self._is_leaf(pos):
            return
        left = self._left_child(pos)
        right = self._right_child(pos)
        if left != -1 and right != -1:
            if self.heap[pos] > self.heap[left] or self.heap[pos] > self.heap[right]:
                if self.heap[left] < self.heap[right]:
                    self._swap(pos, left)
                    self._heapify(left)
                else:
                    self._swap(pos, right)
                    self._heapify(right)
        elif left != -1:
            if self.heap[pos] > self.heap[left]:
                self._swap(pos, left)
                self._heapify(left)

    def _replace(self, val):
        if val > self._peek():
            self.heap[0] = val
            self._heapify(0)
        print self._peek(),


def find_kth_largest(arr, k):
    minHeap = MinHeap(k)
    for i in range(len(arr)):
        minHeap.insert(arr[i])

arr = [10, 20, 11, 70, 50, 40, 100, 5]
k = 3
find_kth_largest(arr, k)
